from models.Field import Field

class Name(Field):
    def __init__(self, value):
        if not value.isalpha() or not value():
            raise ValueError("Name must contain only letters and cannot be empty")
        super().__init__(value)
