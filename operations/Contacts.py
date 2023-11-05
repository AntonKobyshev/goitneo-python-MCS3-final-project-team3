from helpers.decorators import input_error
from models.Record import Record
from helpers.error import RecordNotFound


class ContactsOperations:
    def show_all(book):
        if not book:
            return "Your phone book is empty."
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
    def edit_contact(args, book):
        if len(args) != 3:
            return "❌ Give me name, old phone and new phone please."

        name, old_phone, new_phone = args
        record = book.find(name)
        record.edit_phone(old_phone, new_phone)
        return "✔️ Contact updated."

    @input_error
    def find_contact(args, book):
        search_char = args[0]

        if len(search_char) < 2:
            return "❌ Give me at least 2 characters from the name, please."

        matching_records = []

        for record_name, record in book.data.items():
            if record.contains_char_or_digit(search_char):
                phone_str = ', '.join(phone.value for phone in record.phones)
                info = []
                if record.email is not None:
                    info.append(f"Email: {record.email}")
                if record.address is not None:
                    info.append(f"Address: {record.address}")
                if record.birthday is not None:
                    info.append(f"birthday: {record.birthday}")

                info_str = ', '.join(info)
                if info_str:
                    info_str = f", {info_str}"

                matching_records.append(
                    f"👤 Name: {record.name.value}, Phone(s): {phone_str}{info_str}")

        if not matching_records:
            return "❌ No matching contacts found."

        return "\n".join(matching_records)

    @input_error
    def delete_contact(args, book):
        if len(args) != 1:
            return "Give me name please."

        name = args[0]
        book.delete(name)
        return "✔️ Contact deleted."
