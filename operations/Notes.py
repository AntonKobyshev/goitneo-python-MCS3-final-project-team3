from helpers.decorators import input_error

class NotesOperations:
    def show_all(notes):
        if not notes:
            return "❌ Your notes are empty."

        result = ""
        for note in notes.values():
            result += str(note) + "\n"

        return result if result else "❌ Your notes are empty."

    @input_error
    def add_note(args, notesbook):
        if len(args) < 3:
            return "❌ Give me a title, note text, and at least one tag."
        
        title = args[0]
        text = " ".join(args[1:-1])
        tags = set(args[-1].split(',')) if args[-1].startswith('#') else set()
        notesbook.add_record(title, text, tags)
        return "✔️ Note added with tags." if tags else "✔️ Note added."
    
    @input_error
    def find_notes_by_tag(args, notesbook):
        if len(args) != 1:
            return "❌ Please provide a single tag to search for."
        
        tag = args[0]
        matching_notes = [str(note) for note in notesbook.values() if tag in note.tags]
        return "\\n".join(matching_notes) if matching_notes else "❌ No notes found with that tag."
        
    @input_error
    def find_note(args, notesbook):
        if len(args) != 1:
            return "❌ Please provide a title to search for."
        
        title = args[0]
        matching_notes = [str(note) for note in notesbook.values() if title == note.title]
        return "\\n".join(matching_notes) if matching_notes else "❌ No notes found with that title."
    
    @input_error
    def sort_notes_by_tag(args, notesbook):
        tag = args[0] if args else None
        sorted_notes = notesbook.sort_notes_by_tag(tag)
        result = ""
        for title, note in sorted_notes:
            tags_formatted = ', '.join(sorted(note.tags)) if note.tags else 'No Tags'
            result += f"Title: {title}\nTags: {tags_formatted}\n\n"
        return result.rstrip("\n")

    @input_error
    def edit_note(args, notes):
        if len(args) < 2:
            return "❌ Give me a title, and new text for editing."

        title = args[0]
        new_text = " ".join(args[1:])
        if title in notes:
            note = notes[title]
            note.text = new_text
            return "✔️ Note edited."
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