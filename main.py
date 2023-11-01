from models.AddressBook import AddressBook
from operations.Contacts import ContactsOperations
from operations.Birthdays import BirthdaysOperations
from operations.Phones import PhoneOperations
from operations.Addresses import AdressesOperations
from operations.Emails import EmailsOperations
from helpers.parser import parse_input
from models.Note import Notes
from operations.Notes import NotesOperations

CONTACTS_FILENAME = "contacts.bin"

def main() -> None:
    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)
    notes = {}
    print("🤖 Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("⌨️ Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                book.save_to_file(CONTACTS_FILENAME)
                print("🖐 Good bye!")
                break

            elif command == "hello":
                print("🖐 Hi! How can I help you?")
            elif command == "all":
                print(ContactsOperations.show_all(book))
            elif command == "add":
                print(ContactsOperations.add_contact(args, book))
            elif command == "change":
                print(ContactsOperations.change_contact(args, book))
            elif command == "delete":
                print(ContactsOperations.delete_contact(args, book))
            elif command == "phone":
                print(PhoneOperations.show_phone(args, book))
            elif command == "remove-phone":
                print(PhoneOperations.remove_phone(args, book))
            elif command == "birthdays":
                print(BirthdaysOperations.birthdays(book))
            elif command == "add-birthday":
                print(BirthdaysOperations.add_birthday(args, book))
            elif command == "show-birthday":
                print(BirthdaysOperations.show_birthday(args, book))
            elif command == "add-address":
                print(AdressesOperations.add_address(args, book))
            elif command == "show-address":
                print(AdressesOperations.show_address(args, book))
            elif command == "add-email":
                print(EmailsOperations.add_email(args, book))
            elif command == "show-email":
                print(EmailsOperations.show_email(args, book))
            elif command == "all-notes":
                print(NotesOperations.show_all(notes))
            elif command == "add-note":
                print(NotesOperations.add_note(args, notes))
            elif command == "find-note":
                print(NotesOperations.find_note(args, notes))
            elif command == "edit-note":
                print(NotesOperations.edit_note(args, notes))
            elif command == "delete-note":
                print(NotesOperations.delete_note(args, notes))
            else:
                print("❌ Incorrect command.")
        except KeyboardInterrupt:
            print("\n ❌ Incorrect command.")
        except:
            book.save_to_file(CONTACTS_FILENAME)
            print("❌ Something went wrong.")
            break


if __name__ == "__main__":
    main()
