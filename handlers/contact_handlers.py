"""CLI handler functions for contact management."""

from utils.decorators import input_error
from models.address_book import AddressBook, Record


@input_error
def show_phone(args, book: AddressBook) -> str:
    """Show all phone numbers for the contact named args[0]."""
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    phones = ", ".join(str(p) for p in record.phones) or "—"
    return f"{name}: {phones}"


@input_error
def show_all(args, book: AddressBook) -> str:
    """Return a formatted string of all contacts, or a notice if empty."""
    if not book.data:
        return "Address book is empty."
    contacts = []
    for record in book.data.values():
        contacts.append(str(record))
    return "\n".join(contacts)


@input_error
def add_contact(args, book: AddressBook) -> str:
    """Add a new contact or append a phone to an existing one.

    args: [name, phone]
    """
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
    else:
        record.add_phone(phone)
    return "Contact added."


@input_error
def change_phone(args, book: AddressBook) -> str:
    """Replace old_phone with new_phone for the given contact.

    args: [name, old_phone, new_phone]
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def delete_contact(args, book: AddressBook) -> str:
    """Delete the contact named args[0] from the address book."""
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    book.data.pop(record.name.value)
    return "Contact removed."


@input_error
def add_email(args, book: AddressBook) -> str:
    """Add an email address to an existing contact.

    args: [name, email]
    """
    name, email = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_email(email)
    return "Email added."


@input_error
def add_address(args, book: AddressBook) -> str:
    """Set the address for an existing contact.

    args: [name, address_word1, address_word2, ...]
    """
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_address(address)
    return "Address added."


@input_error
def add_birthday(args, book: AddressBook) -> str:
    """Add a birthday (DD.MM.YYYY) to an existing contact.

    args: [name, DD.MM.YYYY]
    """
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook) -> str:
    """Show the birthday of the contact named args[0]."""
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    if record.birthday is None:
        return "Birthday not set."
    return f"{name}: {record.birthday}"


@input_error
def get_birthdays(args, book: AddressBook) -> str:
    """List contacts whose birthdays fall within the next N days.

    args: [days] — defaults to 7 if omitted.
    Weekends are shifted to the following Monday.
    """
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the next {days} days."
    result = [
        f"{item['name']} -> {item['congratulation_date']}"
        for item in upcoming
    ]
    return "\n".join(result)


@input_error
def find_contact(args, book: AddressBook) -> str:
    """Search contacts by name, phone or email (case-insensitive partial match).

    args: [query_word1, query_word2, ...]
    """
    query = " ".join(args)
    if not query:
        raise ValueError("Enter search query")
    results = book.search(query)
    if not results:
        return "No contacts found."
    return "\n\n".join(str(record) for record in results)
