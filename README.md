This application is a bot assistant developed to manage contacts, notes, and other tasks. It offers the following functionalities:

1. Contact Management:

   - View all contacts.
   - Add a new contact.
   - Search for a contact by name.
   - Edit a contact.
   - Delete a contact.
   - Display a contact's phone numbers.
   - Remove a contact's phone number.

2. Birthday Management:

   - View upcoming birthdays.
   - Add a new birthday.
   - Display information about a birthday.

3. Address Management:

   - Add an address to a contact.
   - Display a contact's address.

4. Email Management:

   - Add an email address to a contact.
   - Display a contact's email address.

5. Note Management:

   - View all notes.
   - Add a new note.
   - Search for a note by keywords.
   - Edit a note.
   - Delete a note.

6. Quit the program and exit.

The program operates in a console-based mode, accepting user commands and executing corresponding actions for managing contacts, birthdays, addresses, email, and notes. It provides the user with command suggestions and logs error information to `app.log`.

The application assists users in managing their contact information and notes, making it a valuable tool for personal data organization.

## Usage

- Add new contact

```
⌨️ Enter a command: add-contact bob 1234567890
✔️ Contact added.
```

- Edit contact

```
⌨️ Enter a command: edit-contact bob 1234567890 1234567899
✔️ Contact updated.
```

- Add a birthday for the contact

```
⌨️ Enter a command: add-birthday bob 25.11.1990
✔️ Birthday added.
```

- Add an email to the contact

```
⌨️ Enter a command: add-email bob bob@gmail.com
✔️ Email added.
```

- Add an address to the contact

```
⌨️ Enter a command: add-address bob Kyiv, Hrushevskogo str
✔️ Address added.

```

- Display all contacts

```
⌨️ Enter a command:  all-contacts
👤 Contact name: anton, phone(s): 1231231231, birthday: 23.12.1989
👤 Contact name: bob, phone(s): 1234567899, email: bob@gmail.com, address: Kyiv, Hrushevskogo str, birthday: 25.11.1990
```

---

- View all notes

```
⌨️ Enter a command: all-notes
📝 Note title: cofee, text: latte contains a lot of calories, tags: [#coffee, #latte]
```

- Add a new note

```
⌨️ Enter a command: add-note coffee latte contains a lot of calories #coffee,#latte
✔️ Note added with tags.
```

- Search for a note by keywords(tag)

```
⌨️ Enter a command: find-notes-by-tag #coffee
📝 Note title: cofee, text: latte contains a lot of calories, tags: [#coffee, #latte]
```

- sort-notes-by-tag #coffee

```
⌨️ Enter a command: sort-notes-by-tag #coffee
Title: cofee
Tags: #coffee, #latte
```

- Search for a note by title.

```
⌨️ Enter a command: find-note cofee
📝 Note title: cofee, text: latte contains a lot of calories, tags: [#latte, #coffee]
```

- Edit a note.

```
⌨️ Enter a command: edit-note coffee new text
✔️ Note edited.
```

- Delete a note.

```
⌨️ Enter a command: delete-note coffee
✔️ Note deleted.
```

- Close the program.

```
⌨️ Enter a command:  close
🖐 Good bye!
```
