from operations.Contacts import ContactsOperations
from operations.Birthdays import BirthdaysOperations
from operations.Phones import PhoneOperations
from operations.Addresses import AddressesOperations
from operations.Emails import EmailsOperations
from operations.Notes import NotesOperations
from helpers.list_of_commands import *

CONTACTS_FILENAME = "contacts.bin"
NOTES_FILENAME = "notes.bin"

def execute_command(command, args, book, notes):
    # contacts block
    if command.lower() == "all-contacts":
        result = ContactsOperations.show_all(book)
    elif command.lower() == "add-contact":
        result = ContactsOperations.add_contact(args, book)
    elif command.lower() == "find-contact":
        result = ContactsOperations.find_contact(args, book)
    elif command.lower() == "edit-contact":
        result = ContactsOperations.edit_contact(args, book)
    elif command.lower() == "delete-contact":
        result = ContactsOperations.delete_contact(args, book)
    elif command.lower() == "show-phone":
        result = PhoneOperations.show_phone(args, book)
    elif command.lower() == "remove-phone":
        result = PhoneOperations.remove_phone(args, book)
        # birthdays block
    elif command.lower() == "show-birthdays":
        try:
            args = int(input("Enter the number of days: "))
            result = BirthdaysOperations.birthdays(book, args)
        except ValueError:
            result = "❌ Invalid number of days. Please enter a valid integer."
    elif command.lower() == "add-birthday":
        result = BirthdaysOperations.add_birthday(args, book)
    elif command.lower() == "show-birthday":
        result = BirthdaysOperations.show_birthday(args, book)
        # address block
    elif command.lower() == "add-address":
        result = AddressesOperations.add_address(args, book)
    elif command.lower() == "show-address":
        result = AddressesOperations.show_address(args, book)
        # email block
    elif command.lower() == "add-email":
        result = EmailsOperations.add_email(args, book)
    elif command.lower() == "show-email":
        result = EmailsOperations.show_email(args, book)
        # notes block
    elif command.lower() == "all-notes":
        result = NotesOperations.show_all(notes)
    elif command.lower() == "add-note":
        result = NotesOperations.add_note(args, notes)
    elif command.lower() == "find-note":
        result = NotesOperations.find_note(args, notes)
    elif command.lower() == "edit-note":
        result = NotesOperations.edit_note(args, notes)
    elif command.lower() == "delete-note":
        result = NotesOperations.delete_note(args, notes)
        # general block
    elif command.lower() == "help":
        result = display_help()
        return result
    elif command.lower() in ["close", "exit"]:
        result = "🖐 Good bye!"
        return result
    elif command.lower() == "hello":
        result = "🖐 Hi! How can I help you?"
    else:
        result = "❌ Incorrect command"

    book.save_to_file(CONTACTS_FILENAME)
    notes.save_to_file(NOTES_FILENAME)

    return result
