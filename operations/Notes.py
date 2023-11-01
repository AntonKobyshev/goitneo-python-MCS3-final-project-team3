from helpers.decorators import input_error
from models.Note import Notes

class NotesOperations:
    def show_all(notes):
        if not notes:
            return "❌ Your notes are empty."

        result = ""
        for note in notes.values():
            result += str(note) + "\n"

        return result if result else "❌ Your notes are empty."

    @input_error
    def add_note(args, notes):
        if len(args) < 2:
            return "❌ Give me a title and note text."

        title = args[0]
        text = " ".join(args[1:])
        new_note = Notes(title, text)
        notes[title] = new_note
        return "✔️ Note added."

    @input_error
    def find_note(args, notes):
        if len(args) < 1:
            return "❌ Give me a search query."

        query = " ".join(args)
        matching_notes = []
        for note in notes.values():
            if query in note.title or query in note.text:
                matching_notes.append(str(note))
        if matching_notes:
            return "\n".join(matching_notes)
        else:
            return "❌ No matching notes found."

    @input_error
    def edit_note(args, notes):
        if len(args) < 3:
            return "❌ Give me a title, old text, and new text for editing."

        title = args[0]
        old_text = args[1]
        new_text = " ".join(args[2:])
        if title in notes:
            note = notes[title]
            if note.text == old_text:
                note.text = new_text
                return "✔️ Note edited."
            else:
                return "❌ The old text does not match the note."
        else:
            return "❌ Note with that title not found."

    @input_error
    def delete_note(args, notes):
        if len(args) < 1:
            return "❌ Give me a title to delete."

        title = args[0]
        if title in notes:
            del notes[title]
            return "✔️ Note deleted."
        else:
            return "❌ Note with that title not found."