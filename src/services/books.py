from pony import orm

from entities import BaseBook, BaseBookWithAuthor
from errors import DoesNotExistError
from models import Book


class BookService:
    @staticmethod
    @orm.db_session
    def get_all() -> tuple[BaseBook]:
        return tuple(map(BaseBook.from_orm, Book.select()))

    @staticmethod
    @orm.db_session
    def get(book_id: int) -> BaseBookWithAuthor:
        if book := Book.get(id=book_id):
            return BaseBookWithAuthor.from_orm(book)
        raise DoesNotExistError
