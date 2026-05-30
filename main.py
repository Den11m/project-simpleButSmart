"""Entry point for the Personal Assistant CLI."""

from utils.parser import parse_input, suggest_command
from models.address_book import AddressBook
from models.notes import NoteBook
from storage.persistence import save_data, load_data
from handlers.note_handlers import (
    add_note,
    show_all_notes,
    show_note,
    find_note,
    edit_note,
    delete_note,
    add_tag,
    remove_tag,
    find_by_tag,
    sort_by_tag,
)
from handlers.contact_handlers import (
    show_phone,
    show_all,
    add_contact,
    change_phone,
    delete_contact,
    add_email,
    add_address,
    add_birthday,
    show_birthday,
    get_birthdays,
    find_contact,
)

NOTE_COMMANDS = {
    "add-note": add_note,
    "show-notes": show_all_notes,
    "show-note": show_note,
    "find-note": find_note,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "add-tag": add_tag,
    "remove-tag": remove_tag,
    "find-by-tag": find_by_tag,
    "sort-by-tag": sort_by_tag,
}

MENU = """
Available commands:

  Contacts:
    add [name] [phone]                - Add contact or add phone to existing
    change [name] [old] [new]         - Change phone number
    delete-contact [name]             - Delete a contact
    phone [name]                      - Show phone(s) of a contact
    all                               - Show all contacts
    add-email [name] [email]          - Add email to a contact
    add-address [name] [address]      - Add address to a contact
    add-birthday [name] [DD.MM.YYYY]  - Add birthday to a contact
    show-birthday [name]              - Show birthday of a contact
    birthdays [days]                  - Show upcoming birthdays within N days
    find [query]                      - Search contacts by name or phone

  Notes:
    add-note [title] [text]           - Add a new note
    show-notes                        - Show all notes
    show-note [title]                 - Show a specific note
    find-note [query]                 - Search notes by text
    edit-note [title] [new text]      - Edit an existing note
    delete-note [title]               - Delete a note
    add-tag [title] [tag]             - Add tag to a note
    remove-tag [title] [tag]          - Remove tag from a note
    find-by-tag [tag]                 - Find notes by tag
    sort-by-tag                       - Show notes sorted by tags

  Other:
    hello                             - Greet the assistant
    help                              - Show this help message
    close / exit                      - Save and exit
"""


def main():
    """Run the main CLI event loop."""
    book = load_data("addressbook.pkl", AddressBook)
    notebook = load_data("notebook.pkl", NoteBook)

    print("Welcome to Personal Assistant!")
    print(MENU)

    try:
        while True:
            user_input = input("Enter command: ").strip()
            if not user_input:
                continue

            command, args = parse_input(user_input)

            if command in ("close", "exit"):
                print("Goodbye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "help":
                print(MENU)

            elif command in NOTE_COMMANDS:
                print(NOTE_COMMANDS[command](args, notebook))
            elif command == "phone":
                print(show_phone(args, book))

            elif command == "all":
                print(show_all(args, book))

            elif command == "add":
                print(add_contact(args, book))

            elif command == "change":
                print(change_phone(args, book))

            elif command == "delete-contact":
                print(delete_contact(args, book))

            elif command == "add-email":
                print(add_email(args, book))

            elif command == "add-address":
                print(add_address(args, book))

            elif command == "add-birthday":
                print(add_birthday(args, book))

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(get_birthdays(args, book))

            elif command == "find":
                print(find_contact(args, book))

            else:
                suggestion = suggest_command(command)

                if suggestion:
                    print(
                        f"Unknown command '{command}'. "
                        f"Did you mean '{suggestion}'?"
                    )
                else:
                    print(
                        f"Unknown command '{command}'. "
                        "Type 'help' to see available commands."
                    )

    finally:
        save_data(book, "addressbook.pkl")
        save_data(notebook, "notebook.pkl")


if __name__ == "__main__":
    main()
