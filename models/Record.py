from models.Name import Name
from models.Phone import Phone
from models.Birthday import Birthday
from models.Address import Address
from models.Email import Email

from copy import copy
from helpers.error import *


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)
        email_str = self.email.value if self.email else ""
        address_str = self.address.value if self.address else ""
        birthday_str = self.birthday.value if self.birthday else ""

        result = f"👤 Contact name: {self.name.value}, phone(s): {phone_str}"

        if email_str:
            result += f", email: {email_str}"

        if address_str:
            result += f", address: {address_str}"

        if address_str:
            result += f", birthday: {birthday_str}"

        return result

    def add_phone(self, new_phone):
        try:
            self.find_phone(new_phone)
        except PhoneNotFound:
            self.phones.append(Phone(new_phone))
        else:
            raise PhoneConflict(self.name, new_phone)

    def remove_phone(self, phone):
        filtered_phone = list(filter(lambda p: p.value != phone, self.phones))

        if len(filtered_phone) == len(self.phones):
            raise PhoneNotFound(self.name, phone)
        else:
            self.phones = filtered_phone

    def edit_phone(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        old_phone = self.find_phone(old_phone)

        try:
            self.find_phone(new_phone.value)
        except PhoneNotFound:
            old_phone.value = copy(new_phone.value)
        else:
            raise PhoneConflict(self.name.value, new_phone.value)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

        raise PhoneNotFound(self.name, phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday

    def add_address(self, address):
        self.address = Address(address)

    def show_address(self):
        return self.address

    def add_email(self, email):
        self.email = Email(email)

    def show_email(self):
        return self.email
