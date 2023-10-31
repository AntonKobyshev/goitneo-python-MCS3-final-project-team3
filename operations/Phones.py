from helpers.decorators import input_error

class PhoneOperations:
    @input_error
    def show_phone(args, book):
        name = args[0]
        return book.find(name)

    @input_error
    def remove_phone(args, book):
        name, phone = args
        record = book.find(name)
        record.remove_phone(phone)
        return "✔️ Phone removed."