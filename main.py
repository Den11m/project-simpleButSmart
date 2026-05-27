"""Entry point for the Personal Assistant CLI."""

from utils.parser import parse_input
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

from handlers.contact_handlers import (show_phone,
                                        show_all, 
                                        add_contact, 
                                        change_contact, 
                                        delete_contact, 
                                        add_email, 
                                        add_address, 
                                        add_birthday,
                                        show_birthday,
                                        birthdays,
                                        find)
MENU = """
Commands:
  Contacts : add, change, delete-contact, phone, all
             add-email, add-address, add-birthday, show-birthday, birthdays, find
  Notes    : add-note, show-notes, show-note, find-note, edit-note, delete-note
             add-tag, remove-tag, find-by-tag, sort-by-tag
  Other    : help, hello, close / exit
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
                print(change_contact(args, book))

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
                print(birthdays(args, book))

            elif command == "find":
                print(find(args, book))

            else:
                print(f"Unknown command '{command}'. Type 'help' to see available commands.")

    finally:
        save_data(book, "addressbook.pkl")
        save_data(notebook, "notebook.pkl")


if __name__ == "__main__":
    main()
