from enum import Enum


class Genre(str, Enum):
    adventure = "adventure"
    autobiography = "autobiography"
    biography = "biography"
    fantasy = "fantasy"
    history = "history"
    horror = "horror"
    mystery = "mystery"
    poetry = "poetry"
    romance = "romance"
    sci_fi = "sci_fi"
    thriller = "thriller"


class UserStatus(str, Enum):
    inactive = "inactive"
    active = "active"
    disabled = "disabled"
