import logging
from models.AddressBook import AddressBook
from operations.Contacts import ContactsOperations
from operations.Birthdays import BirthdaysOperations
from operations.Phones import PhoneOperations
from operations.Addresses import AddressesOperations
from operations.Emails import EmailsOperations
from helpers.parser import parse_input

CONTACTS_FILENAME = "contacts.bin"


def execute_command(command, args, book):
    if command.lower() == "all":
        result = ContactsOperations.show_all(book)
    elif command.lower() == "add":
        result = ContactsOperations.add_contact(args, book)
    elif command.lower() == "change":
        result = ContactsOperations.change_contact(args, book)
    elif command.lower() == "delete":
        result = ContactsOperations.delete_contact(args, book)
    elif command.lower() == "phone":
        result = PhoneOperations.show_phone(args, book)
    elif command.lower() == "remove-phone":
        result = PhoneOperations.remove_phone(args, book)
    elif command.lower() == "birthdays":
        result = BirthdaysOperations.birthdays(book)
    elif command.lower() == "add-birthday":
        result = BirthdaysOperations.add_birthday(args, book)
    elif command.lower() == "show-birthday":
        result = BirthdaysOperations.show_birthday(args, book)
    elif command.lower() == "add-address":
        result = AddressesOperations.add_address(args, book)
    elif command.lower() == "show-address":
        result = AddressesOperations.show_address(args, book)
    elif command.lower() == "add-email":
        result = EmailsOperations.add_email(args, book)
    elif command.lower() == "show-email":
        result = EmailsOperations.show_email(args, book)
    else:
        result = "❌ Incorrect command."

    book.save_to_file(CONTACTS_FILENAME)

    return result


def main() -> None:
    logging.basicConfig(filename='app.log', level=logging.INFO)

    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)

    print("🤖 Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("⌨️ Enter a command: ")
            command, *args = parse_input(user_input)
            result = execute_command(command, args, book)
            print(result)

        except KeyboardInterrupt:
            print("\n❌ Incorrect command.")
        except Exception as e:
            logging.error(f"Error: {e}")
            print("❌ Something went wrong. Check the log for details.")
            break


if __name__ == "__main__":
    main()
