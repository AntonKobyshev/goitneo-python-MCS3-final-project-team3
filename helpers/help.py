def display_help():
    help_text = """
    Available commands:
    hello - Greet the bot and initiate a conversation
    all-contacts - Show all contacts
    add-contact [name] [phone] - Add a contact
    find-contact [few characters or numbers for search] - Find a contact by params
    edit-contact [name] [old-phone] [new-phone] - Edit a contact
    delete-contact [name] - Delete a contact
    show-phone [name] - Show phone number of a contact
    remove-phone [name] [phone] - Remove phone number from a contact
    show-birthdays ↵ [number of days] - Show upcoming birthdays by specifying the number of days
    add-birthday [name] [date] - Add a birthday to a contact
    show-birthday [name] - Display the birthday of a specific contact
    add-address [name] [address] - Add an address to a contact
    add-phone [name] [phone] - Add an additional phone to a contact
    show-address [name] - Display the address of a specific contact
    add-email [name] [email] - Add an email address to a contact
    show-email [name] - Display the email address of a specific contact
    all-notes - Show all the notes stored in the assistant bot
    add-note [title] [content] - Add a new note
    add-note [title] [content] [#tag] - Add a new note with tag
    find-note [keyword] - Search for a note by title containing a specific keyword or phrase 
    find-notes-by-tag [#tag] - Search for a note by #tag
    sort-notes-by-tag [#tag] - Sort notes by tag
    edit-note [title] [new-content] - Edit an existing note
    delete-note [title] - Delete a specific note by specifying its ID
    close/exit - Exit the program
    """
    return help_text
