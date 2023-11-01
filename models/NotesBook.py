import pickle
from models.Birthday import Birthday

from pathlib import Path
from datetime import datetime
from collections import UserDict, defaultdict
from helpers.weekdays_list import WEEKDAYS
from helpers.error import *


class NotesBook(UserDict):
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

    def save_to_file(self, filename):
        with open(self.__PATH_CONTACTS_DB / filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filename):
        path = self.__PATH_CONTACTS_DB / filename

        if not path.exists():
            return

        with open(path, "rb") as fh:
            self.data = pickle.load(fh)
