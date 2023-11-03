import logging
from helpers.execute_commands import execute_command
from models.AddressBook import AddressBook
from models.NotesBook import NotesBook
from helpers.parser import parse_input
from helpers.command_helper import get_suggested_commands


CONTACTS_FILENAME = "contacts.bin"
NOTES_FILENAME = "notes.bin"

def main() -> None:
    logging.basicConfig(filename='app.log', level=logging.INFO)
    notes = NotesBook()
    book = AddressBook()
    book.read_from_file(CONTACTS_FILENAME)
    notes.read_from_file(NOTES_FILENAME)

    print("🤖 Welcome to the assistant bot! Please input help to see all commands.")

    while True:
        try:
            user_input = input("⌨️ Enter a command: ")
            command, *args = parse_input(user_input)

            available_commands = [
                "all-contacts", "add-contact", "find-contact", "edit-contact", "delete-contact", "show-phone", "remove-phone", "show-birthdays",
                "add-birthday", "show-birthday", "add-address", "show-address", "add-email",
                "show-email", "all-notes", "add-note", "find-note", "find-notes-by-tag", "edit-note", "delete-note",
                "close", "exit", "hello", "help"
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
