import pickle

from pathlib import Path
from datetime import datetime
from copy import copy
from collections import UserDict, defaultdict
from helpers.weekdays_list import WEEKDAYS
from helpers.error import *


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise IncorrectPhone("☎️ The phone number must be 10 numbers.")

        super().__init__(value)


class Birthday(Field):
    _BIRTHDAY_DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, value):
        try:
            datetime.strptime(value, Birthday._BIRTHDAY_DATE_FORMAT)
        except ValueError:
            raise IncorrectBirthday("📅 Birthday must be 'DD.MM.YYYY' format.")
        else:
            super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"👤 Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

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


class AddressBook(UserDict):
    __PATH_CONTACTS_DB = Path(__file__).parent / "db"

    def __str__(self):
        return "".join([f"{record}\n" for record in self.data.values()]).rstrip("\n")

    def add_record(self, record):
        name = record.name.value

        if name in self.data:
            raise RecordConflict(name)
        else:
            self.data[name] = record

    def find(self, name):
        if not name in self.data:
            raise RecordNotFound(name)
        else:
            return self.data[name]

    def delete(self, name):
        if not name in self.data:
            raise RecordNotFound(name)
        else:
            self.data.pop(name)

    def get_birthdays_per_week(self):
        grouped_users = defaultdict(list)

        today = datetime.today().date()

        for record in self.data.values():
            name = record.name.value
            birthday = record.birthday
            if birthday is None:
                continue
            birthday_date = datetime.strptime(
                birthday.value, Birthday._BIRTHDAY_DATE_FORMAT
            ).date()
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                next_year = birthday_this_year.year + 1
                birthday_this_year = birthday_this_year.replace(year=next_year)

            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                weekday = birthday_this_year.weekday()
                if weekday == 5 or weekday == 6:
                    grouped_users[WEEKDAYS[0]].append(name)
                    continue

                grouped_users[birthday_this_year.strftime("%A")].append(name)

        birthdays_per_week = list()

        for weekday in WEEKDAYS:
            users_list = grouped_users[weekday]
            if users_list:
                weekday_list = f"{weekday}: {', '.join(users_list)}"
                birthdays_per_week.append(weekday_list)

        return birthdays_per_week

    def save_to_file(self, filename):
        with open(self.__PATH_CONTACTS_DB / filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filename):
        path = self.__PATH_CONTACTS_DB / filename

        if not path.exists():
            return

        with open(path, "rb") as fh:
            self.data = pickle.load(fh)
