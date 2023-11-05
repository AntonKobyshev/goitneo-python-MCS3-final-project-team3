from helpers.decorators import input_error


class AddressesOperations:

    @input_error
    def add_address(args, book):
        if len(args) < 2:
            return "❌ Give me a name and an address please."

        name = args[0]
        address = " ".join(args[1:])

        record = book.find(name)
        record.add_address(address)
        return "✔️ Address added."

    @input_error
    def show_address(args, book):
        name = args[0]
        record = book.find(name)
        address = record.show_address()
        if address:
            return address
        else:
            return "❌ This contact does not have address recorded."
