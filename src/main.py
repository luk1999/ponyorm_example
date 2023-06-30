from ast import For
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from errors import ConflictError, DoesNotExistError, ForbiddenError
from routes import users
from services.authors import AuthorService
from services.books import BookService

app = FastAPI()


@app.exception_handler(DoesNotExistError)
async def does_not_exist_handler(request: Request, exc: DoesNotExistError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"detail": "Not Found"})


@app.exception_handler(ForbiddenError)
async def forbidden(request: Request, exc: ForbiddenError):
    return JSONResponse(status_code=HTTPStatus.FORBIDDEN, content={"detail": str(exc)})


@app.exception_handler(ConflictError)
async def already_exists_handler(request: Request, exc: ConflictError):
    return JSONResponse(status_code=HTTPStatus.CONFLICT, content={"detail": str(exc)})


@app.get("/")
async def root():
    return {"message": "Ready"}


@app.get("/authors")
async def get_authors():
    return AuthorService.get_all()


@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    return AuthorService.get(author_id)


@app.get("/books")
async def get_books():
    return BookService.get_all()


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return BookService.get(book_id)


app.include_router(users.router)
