from helpers.error import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name please."
        except IndexError:
            return "Give me name and phone please."
        except ValueError:
            return "Give me name and phone please."
        except IncorrectPhone as error:
            return error.message
        except IncorrectBirthday as error:
            return error.message
        except RecordNotFound as error:
            return f"A person with name {error.name} is not in your phone book."
        except RecordConflict as error:
            return f"A person with name {error.name} already exists."
        except PhoneNotFound as error:
            return f"{error.name}`s record doesn`t contain {error.phone} phone number."
        except PhoneConflict as error:
            return f"{error.name}`s record contains {error.phone} phone number."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return inner
