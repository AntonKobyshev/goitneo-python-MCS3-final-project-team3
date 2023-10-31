class IncorrectPhone(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class IncorrectBirthday(Exception):
    def __init__(self, message, *args):
        super().__init__(*args)
        self.message = message


class RecordNotFound(Exception):
    def __init__(self, name, *args):
        super().__init__(*args)
        self.name = name


class RecordConflict(Exception):
    def __init__(self, name, *args):
        super().__init__(*args)
        self.name = name


class PhoneNotFound(Exception):
    def __init__(self, name, phone, *args):
        super().__init__(*args)
        self.name = name
        self.phone = phone


class PhoneConflict(Exception):
    def __init__(self, name, phone, *args):
        super().__init__(*args)
        self.name = name
        self.phone = phone
