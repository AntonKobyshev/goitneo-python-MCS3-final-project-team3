import re
from models.Field import Field


class Email(Field):
    def __init__(self, value):
        if not self.is_valid_email(value):
            raise ValueError(
                "Incorrect email address. Email should have format xxx@xxx.xxx")
        super().__init__(value)

    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None
