from http import HTTPStatus

from fastapi import APIRouter, Response

from errors import ForbiddenError
from services.users import BaseUserCreate, UserError, UserService

router = APIRouter(prefix="/users")


@router.get("/")
async def get_users():
    return UserService.get_all()


@router.get("/{user_id}")
async def get_user(user_id: int):
    return UserService.get(user_id)


@router.post("/", status_code=HTTPStatus.CREATED)
async def add_user(user: BaseUserCreate):
    UserService.add(user)
    return {"detail": "Created"}


@router.post("/activate", status_code=HTTPStatus.ACCEPTED)
async def activate_user(username: str):
    try:
        return UserService.activate(username) or {"detail": "Activated"}
    except UserError as e:
        raise ForbiddenError(e)


@router.post("/deactivate", status_code=HTTPStatus.ACCEPTED)
async def deactivate_user(username: str):
    try:
        return UserService.deactivate(username) or {"detail": "Deactivated"}
    except UserError as e:
        raise ForbiddenError(e)


@router.get(".txt")
async def get_user_names():
    return Response(content="\n".join(map(lambda u: u.username, UserService.get_all())), media_type="text")
