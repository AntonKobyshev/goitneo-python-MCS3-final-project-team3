import difflib

def get_suggested_commands(user_input, available_commands):
    prefix_matches = [cmd for cmd in available_commands if cmd.startswith(user_input)]
    if prefix_matches:
        return prefix_matches
    suggested_commands = difflib.get_close_matches(user_input, available_commands, n = 6, cutoff = 0.5)
    return suggested_commands