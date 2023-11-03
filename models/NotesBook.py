import pickle

from pathlib import Path
from collections import UserDict
from models.Note import Notes
from helpers.error import *


class NotesBook(UserDict):
    __PATH_NOTES_DB = Path(__file__).parent.parent / "db"

    def __str__(self):
        return "".join([f"{record}\n" for record in self.data.values()]).rstrip("\n")

    def add_record(self, title, text, tags=None):
        if title in self.data:
            raise RecordConflict(title)
        else:
            self.data[title] = Notes(title, text, tags)
    
    def find_by_tag(self, tag):
        return [record for record in self.data.values() if tag in record.tags]
    
    # def sort_notes_by_tag(self, tag=None):
        if tag:
            notes_with_tag = [(title, note) for title, note in self.data.items() if tag in note.tags]
            return sorted(notes_with_tag, key=lambda item: item[0]) 
        else:
            return sorted(self.data.items(), key=lambda item: item[0])

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
        with open(self.__PATH_NOTES_DB / filetitle, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filetitle):
        path = self.__PATH_NOTES_DB / filetitle
        if path.exists():
            with open(path, "rb") as fh:
                self.data.update(pickle.load(fh).data)
