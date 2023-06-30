from datetime import date
from pony import orm

from enums import Genre, UserStatus
from models import Author, Book, User
from services.users import UserService


@orm.db_session
def init_db():
    clarke = Author(first_name="Arthur Charles ", last_name="Clarke", date_of_birth=date(1917, 12, 16))
    king = Author(first_name="Stephen", last_name="King", date_of_birth=date(1947, 9, 21))
    grisham = Author(first_name="John", last_name="Grisham", date_of_birth=date(1955, 2, 8))

    Book(author=clarke, title="2001: A Space Odyssey", year=1968, genre=Genre.sci_fi)
    Book(author=king, title="It", year=1986, genre=Genre.horror)
    Book(author=king, title="The Shining", year=1977, genre=Genre.horror)
    gunslinger = Book(author=king, title="The Gunslinger", year=1982, genre=Genre.fantasy)
    pelican = Book(author=grisham, title="The Pelican Brief", year=1992, genre=Genre.thriller)
    rainmaker = Book(author=grisham, title="The Rainmaker", year=1995, genre=Genre.thriller)

    smith = User(
        username="john_smith",
        password=UserService.encode_password("12345678"),
        first_name="John",
        last_name="Smith",
        status=UserStatus.active,
    )
    smith.books.add(rainmaker)
    smith.books.add(gunslinger)
    rambo = User(
        username="rambo",
        password=UserService.encode_password("abcdefgh"),
        status=UserStatus.active,
    )
    rambo.books.add(pelican)
    smith = User(
        username="test_account",
        password=UserService.encode_password("abcd1234"),
        first_name="Test",
        last_name="Account",
        status=UserStatus.disabled,
    )

    orm.commit()


if __name__ == "__main__":
    print("Initializing db data...")
    init_db()
    print("Done.")
