import hashlib

from pony import orm
from pydantic import BaseModel, validator

from entities import BaseUser, BaseUserWithBooks
from enums import UserStatus
from errors import DoesNotExistError
from models import User


MIN_PASS_LEN = 8


def encode_password(password: str) -> str:
    """Just for demo purpose. It should not be used in real-world app!"""
    return hashlib.md5(password.encode()).hexdigest()


class UserError(Exception):
    ...


class UserCannotBeActivatedError(UserError):
    ...


class UserCannotBeDisabledError(UserError):
    ...


class BaseUserCreate(BaseModel):
    username: str
    first_name: str | None = None
    last_name: str | None = None
    password: str

    @validator("password")
    def password_validator(cls, password: str) -> str:
        if not password or len(password) < MIN_PASS_LEN:
            raise ValueError(f"Password must have at least {MIN_PASS_LEN} chars")

        return encode_password(password)

    @validator("username")
    @orm.db_session
    def username_validator(cls, username: str) -> str:
        if User.get(username=username):
            raise ValueError("User already exists")

        return username


class UserService:
    encode_password = encode_password

    @staticmethod
    @orm.db_session
    def get_all() -> tuple[BaseUser]:
        return tuple(map(BaseUser.from_orm, User.select()))

    @staticmethod
    @orm.db_session
    def get(user_id: int) -> BaseUserWithBooks:
        if user := User.get(id=user_id):
            return BaseUserWithBooks.from_orm(user)
        raise DoesNotExistError

    @staticmethod
    @orm.db_session
    def add(user: BaseUserCreate) -> BaseUser:
        user = User(**dict(user))
        orm.commit()
        return BaseUser(**user.to_dict())

    @staticmethod
    @orm.db_session
    def activate(username: str) -> None:
        if user := User.get(lambda u: u.username.lower() == username.lower()):
            if user.status != UserStatus.inactive:
                raise UserCannotBeActivatedError("User cannot be activated")

            user.status = UserStatus.active
            orm.commit()
            return

        raise DoesNotExistError

    @staticmethod
    @orm.db_session
    def deactivate(username: str) -> None:
        if user := User.get(lambda u: u.username.lower() == username.lower()):
            if user.status != UserStatus.active:
                raise UserCannotBeDisabledError("User cannot be disabled")

            user.status = UserStatus.disabled
            orm.commit()
            return

        raise DoesNotExistError
