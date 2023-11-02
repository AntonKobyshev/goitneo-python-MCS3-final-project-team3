def display_help():
    help_text = """
    Available commands:
    hello - Greet the bot and initiate a conversation
    all-contacts - Show all contacts
    add-contact [name] [phone] - Add a contact
    find-contact [name or few characters] - Find a contact by params
    edit-contact [name] [old-phone] [new-phone] - Edit a contact
    delete-contact [name] - Delete a contact
    show-phone [name] - Show phone number of a contact
    remove-phone [name] - Remove phone number from a contact
    show-birthdays ↵ [number of days] - Show upcoming birthdays by specifying the number of days
    add-birthday [name] [date] - Add a birthday to a contact
    show-birthday [name] - Display the birthday of a specific contact
    add-address [name] [address] - Add an address to a contact
    show-address [name] - Display the address of a specific contact
    add-email [name] [email] - Add an email address to a contact
    show-email [name] - Display the email address of a specific contact
    all-notes - Show all the notes stored in the assistant bot
    add-note [title] [content] - Add a new note
    find-note [keyword] - Search for a note containing a specific keyword or phrase
    edit-note [title] [old-content] [new-content] - Edit an existing note
    delete-note [title] - Delete a specific note by specifying its ID
    close/exit - Exit the program
    """
    return help_text