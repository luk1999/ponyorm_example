from datetime import date

from pony import orm

from config import DATABASE
from enums import UserStatus


db = orm.Database()
db.bind(**DATABASE)


class Author(db.Entity):
    first_name = orm.Required(str, 100)
    last_name = orm.Required(str, 100)
    date_of_birth = orm.Required(date)
    books = orm.Set("Book")

    orm.composite_key(first_name, last_name, date_of_birth)


class Book(db.Entity):
    author = orm.Required(Author)
    title = orm.Required(str, 100)
    year = orm.Required(int)
    genre = orm.Required(str, 30)
    borrowed_by = orm.Set("User")

    orm.composite_key(author, title)


class User(db.Entity):
    username = orm.Required(str, 50, unique=True)
    password = orm.Required(str, 32)
    first_name = orm.Optional(str, 100)
    last_name = orm.Optional(str, 100)
    status = orm.Required(str, 30, default=UserStatus.inactive.value)
    books = orm.Set(Book)


db.generate_mapping(create_tables=True)
