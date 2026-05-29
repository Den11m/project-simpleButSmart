"""Input parsing utilities."""
from difflib import get_close_matches


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

ALL_COMMANDS = [
    "add",
    "change",
    "delete-contact",
    "phone",
    "add-email",
    "add-address",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "find",
    "all",
    "add-note",
    "show-notes",
    "show-note",
    "find-note",
    "edit-note",
    "delete-note",
    "add-tag",
    "remove-tag",
    "find-by-tag",
    "sort-by-tag",
    "hello",
    "close",
    "exit",
    "help",
]


def suggest_command(user_input: str) -> str | None:
    matches = get_close_matches(
        user_input.lower(),
        ALL_COMMANDS,
        n=1,
        cutoff=0.6,
    )
    return matches[0] if matches else None