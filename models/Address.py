from models.Field import Field
from helpers.error import IncorrectAddress


class Address(Field):
    def __init__(self, value):
        if not value:
            raise IncorrectAddress("Address cannot be empty")
        super().__init__(value)
