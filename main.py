"""Entry point for the Personal Assistant CLI."""

from utils.parser import parse_input
from models.address_book import AddressBook
from models.notes import NoteBook
from storage.persistence import save_data, load_data

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

            else:
                print(f"Unknown command '{command}'. Type 'help' to see available commands.")

    finally:
        save_data(book, "addressbook.pkl")
        save_data(notebook, "notebook.pkl")


if __name__ == "__main__":
    main()
