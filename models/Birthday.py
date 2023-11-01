from models.Field import Field
from datetime import datetime
from helpers.error import IncorrectBirthday


class Birthday(Field):
    _BIRTHDAY_FORMAT = "%d.%m.%Y"

    def __init__(self, value):
        try:
            datetime.strptime(value, Birthday._BIRTHDAY_FORMAT)
        except ValueError:
            raise IncorrectBirthday("📅 Birthday must be 'DD.MM.YYYY' format.")
        else:
            super().__init__(value)
