from models.Field import Field
from helpers.errors import IncorrectPhone


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise IncorrectPhone("☎️ The phone number must be 10 numbers.")

        super().__init__(value)
