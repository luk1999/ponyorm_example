from pony import orm

from entities import BaseAuthor, BaseAuthorWithBooks
from errors import DoesNotExistError
from models import Author


class AuthorService:
    @staticmethod
    @orm.db_session
    def get_all() -> tuple[BaseAuthor]:
        return tuple(map(BaseAuthor.from_orm, Author.select()))

    @staticmethod
    @orm.db_session
    def get(author_id: int) -> BaseAuthorWithBooks:
        if author := Author.get(id=author_id):
            return BaseAuthorWithBooks.from_orm(author)
        raise DoesNotExistError
