from helpers.decorators import input_error


class BirthdaysOperations:

    @input_error
    def birthdays(book, days_until_birthday):
        birthdays_in_range = book.get_birthdays(days_until_birthday)
        if birthdays_in_range:
            return "\n".join(birthdays_in_range)
        else:
            return "❌ No birthdays for the specified number of days."

    @input_error
    def add_birthday(args, book):
        if len(args) != 2:
            return "❌ Give me name and birthday date please."

        name, birthday_date = args
        record = book.find(name)
        record.add_birthday(birthday_date)
        return "✔️ Birthday added."

    @input_error
    def show_birthday(args, book):
        name = args[0]
        record = book.find(name)
        birthday_date = record.show_birthday()
        if birthday_date:
            return birthday_date
        else:
            return "❌ This contact does not have a birthday recorded."
