import re
from models.Field import Field


class Name(Field):
    def __init__(self, value):
        if not self.is_valid_name(value):
            raise ValueError(
                "Name must contain only letters and cannot be empty")
        super().__init__(value)

    def is_valid_name(self, name):
        pattern = r"^[a-zA-Z\s]+$"
        return bool(re.match(pattern, name))
