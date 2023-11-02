import logging
from models.AddressBook import AddressBook
from models.NotesBook import NotesBook
from operations.Contacts import ContactsOperations
from operations.Birthdays import BirthdaysOperations
from operations.Phones import PhoneOperations
from operations.Addresses import AddressesOperations
from operations.Emails import EmailsOperations
from helpers.parser import parse_input
from operations.Notes import NotesOperations
from helpers.command_helper import get_suggested_commands


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


def main() -> None:
    logging.basicConfig(filename='app.log', level=logging.INFO)
    notes = NotesBook()
    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)
    notes.read_from_file(NOTES_FILENAME)

    print("🤖 Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("⌨️ Enter a command: ")
            command, *args = parse_input(user_input)

            available_commands = [
                "all-contacts", "add-contact", "find-contact", "edit-contact", "delete-contact", "show-phone", "remove-phone", "show-birthdays",
                "add-birthday", "show-birthday", "add-address", "show-address", "add-email",
                "show-email", "all-notes", "add-note", "find-note", "edit-note", "delete-note",
                "close", "exit", "hello"
            ]

            if command.lower() in available_commands:
                result = execute_command(command, args, book, notes)
                print(result)

                if result == "🖐 Good bye!":
                    break
            else:
                suggested_commands = get_suggested_commands(
                    command, available_commands)
                if suggested_commands:
                    print("Did you mean:", ', '.join(suggested_commands), "?")
                else:
                    print("🤔 Command not found. Try again.")

        except KeyboardInterrupt:
            print("\n❌ Incorrect command.")
        except Exception as e:
            logging.error(f"Error: {e}")
            print("❌ Something went wrong. Check the log for details.")
            break


if __name__ == "__main__":
    main()
