import pickle

from pathlib import Path
from collections import UserDict
from helpers.error import *


class NotesBook(UserDict):
    __PATH_CONTACTS_DB = Path(__file__).parent.parent / "db"

    def __str__(self):
        return "".join([f"{record}\n" for record in self.data.values()]).rstrip("\n")

    def add_record(self, record):
        title = record.title.value

        if title in self.data:
            raise RecordConflict(title)
        else:
            self.data[title] = record

    def find(self, title):
        if not title in self.data:
            raise RecordNotFound(title)
        else:
            return self.data[title]

    def delete(self, title):
        if not title in self.data:
            raise RecordNotFound(title)
        else:
            self.data.pop(title)

    def save_to_file(self, filetitle):
        with open(self.__PATH_CONTACTS_DB / filetitle, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filetitle):
        path = self.__PATH_CONTACTS_DB / filetitle

        if not path.exists():
            return

        with open(path, "rb") as fh:
            self.data = pickle.load(fh)
