"""Input parsing utilities."""


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Split raw user input into (command, args).

    Command is lowercased and stripped. Args are returned as a list of strings.
    Returns ('', []) for empty input.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args
