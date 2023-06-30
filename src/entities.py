from datetime import date

from pydantic import BaseModel, validator

from enums import Genre


class BaseBook(BaseModel):
    id: int | None
    title: str
    year: int
    genre: Genre

    class Config:
        orm_mode = True


class BaseAuthor(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    date_of_birth: date

    class Config:
        orm_mode = True


class BaseAuthorWithBooks(BaseAuthor):
    books: list[BaseBook]

    class Config:
        orm_mode = True

    @validator("books", pre=True, allow_reuse=True)
    def load_books(cls, books) -> list[BaseBook]:
        return [book.to_dict() for book in books]


class BaseBookWithAuthor(BaseBook):
    author: BaseAuthor


class BaseUser(BaseModel):
    id: int | None
    username: str
    first_name: str | None = None
    last_name: str | None = None
    status: str

    class Config:
        orm_mode = True


class BaseUserWithBooks(BaseUser):
    books: list[BaseBook]

    @validator("books", pre=True, allow_reuse=True)
    def load_books(cls, books) -> list[BaseBookWithAuthor]:
        return list(map(BaseBookWithAuthor.from_orm, books))
