import pickle
from models.Birthday import Birthday

from pathlib import Path
from datetime import datetime
from collections import UserDict, defaultdict
from helpers.weekdays_list import WEEKDAYS
from helpers.error import *


class AddressBook(UserDict):
    __PATH_CONTACTS_DB = Path(__file__).parent.parent / "db"
    WEEKDAYS = WEEKDAYS

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

    def get_birthdays_per_week(self, days_until_birthday):
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

            if 0 <= delta_days <= days_until_birthday:
                weekday = birthday_this_year.weekday()
                if weekday == 5 or weekday == 6:
                    day_of_week = self.WEEKDAYS[0]
                else:
                    day_of_week = birthday_this_year.strftime("%A")
                formatted_date = birthday_this_year.strftime("%Y-%m-%d")
                grouped_users[day_of_week].append(f"{name} ({formatted_date})")

        birthdays_per_week = list()

        for day_of_week in self.WEEKDAYS:
            users_list = grouped_users[day_of_week]
            if users_list:
                user_info = "\n".join(users_list)
                weekdays_list = f"{day_of_week}:\n{user_info}"
                birthdays_per_week.append(weekdays_list)

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
