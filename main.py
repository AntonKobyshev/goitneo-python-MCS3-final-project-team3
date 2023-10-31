from models.AddressBook import AddressBook
from controllers.controllers import ContactsCtrl
from helpers.parser import parse_input

CONTACTS_FILENAME = "contacts.bin"


def main() -> None:
    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)
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
                print(ContactsCtrl.show_all(book))
            elif command == "add":
                print(ContactsCtrl.add_contact(args, book))
            elif command == "change":
                print(ContactsCtrl.change_contact(args, book))
            elif command == "delete":
                print(ContactsCtrl.delete_contact(args, book))
            elif command == "phone":
                print(ContactsCtrl.show_phone(args, book))
            elif command == "remove-phone":
                print(ContactsCtrl.remove_phone(args, book))
            elif command == "birthdays":
                print(ContactsCtrl.birthdays(book))
            elif command == "add-birthday":
                print(ContactsCtrl.add_birthday(args, book))
            elif command == "show-birthday":
                print(ContactsCtrl.show_birthday(args, book))
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
