from helpers.error import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IncorrectPhone as error:
            return error.message
        except IncorrectBirthday as error:
            return error.message
        except IncorrectEmail as error:
            return error.message
        except IncorrectName as error:
            return error.message
        except IncorrectAddress as error:
            return error.message
        except RecordNotFound as error:
            return f"A person with name {error.name} is not in your phone book."
        except RecordConflict as error:
            return f"A person with name {error.name} already exists."
        except PhoneNotFound as error:
            return f"{error.name}`s record doesn`t contain {error.phone} phone number."
        except PhoneConflict as error:
            return f"{error.name}`s record contains {error.phone} phone number."
        except KeyError as e:
            return f"KeyError: {str(e)}"
        except IndexError as e:
            return f"IndexError: {str(e)}"
        except ValueError as e:
            return f"ValueError: {str(e)}"
        except Exception as e:
            return f"ExceptionError: {str(e)}"

    return inner
