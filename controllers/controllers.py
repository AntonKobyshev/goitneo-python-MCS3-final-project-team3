from helpers.decorators import input_error
from models.Record import Record
from helpers.error import RecordNotFound


class ContactsCtrl:
    def show_all(book):
        if not book:
            return "❌ Your phone book is empty."
        return book

    @input_error
    def add_contact(args, book):
        name, phone = args
        try:
            record = book.find(name)
        except RecordNotFound:
            new_record = Record(name)
            new_record.add_phone(phone)
            book.add_record(new_record)
        else:
            record.add_phone(phone)

        return "✔️ Contact added."

    @input_error
    def change_contact(args, book):
        if len(args) != 3:
            return "❌ Give me name, old phone and new phone please."

        name, old_phone, new_phone = args
        record = book.find(name)
        record.edit_phone(old_phone, new_phone)
        return "✔️ Contact updated."

    @input_error
    def delete_contact(args, book):
        name = args[0]
        book.delete(name)
        return "✔️ Contact deleted."

    @input_error
    def show_phone(args, book):
        name = args[0]
        return book.find(name)

    @input_error
    def remove_phone(args, book):
        name, phone = args
        record = book.find(name)
        record.remove_phone(phone)
        return "✔️ Phone removed."

    @input_error
    def birthdays(book):
        birthdays_per_week = book.get_birthdays_per_week()
        if birthdays_per_week:
            return "\n".join(book.get_birthdays_per_week())
        else:
            return "❌ No birthdays for the next week."

    @input_error
    def add_birthday(args, book):
        if len(args) != 2:
            return "❌ Give me name and birthday date please."

        name, birthday_date = args
        record = book.find(name)
        record.add_birthday(birthday_date)
        return "✔️ Birthday added."

    @input_error
    def show_birthday(args, book):
        name = args[0]
        record = book.find(name)
        birthday_date = record.show_birthday()
        if birthday_date:
            return birthday_date
        else:
            return "❌ This contact does not have a birthday recorded."
