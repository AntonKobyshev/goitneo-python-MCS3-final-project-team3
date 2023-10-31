from helpers.decorators import input_error


class EmailsOperations:

    @input_error
    def add_email(args, book):
        if len(args) != 2:
            return "❌ Give me name email please."

        name, email = args
        record = book.find(name)
        record.add_email(email)
        return "✔️ Email added."

    @input_error
    def show_email(args, book):
        name = args[0]
        record = book.find(name)
        email = record.show_email()
        if email:
            return email
        else:
            return "❌ This contact does not have email recorded."
