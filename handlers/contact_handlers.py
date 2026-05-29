"""CLI handler functions for contact management — stub. Implemented in TASK-5."""

from utils.decorators import input_error
from models.address_book import AddressBook, Record

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    
    phones = ", ".join(str(p) for p in record.phones) or "—"
    return f"{name}: {phones}"

@input_error    
def show_all(args, book: AddressBook):
    contacts = []
    if not book.data:
        return "Address book is empty."
    for record in book.data.values():
        contacts.append(str(record))
    return "\n".join(contacts)

@input_error
def add_contact(args, book: AddressBook):
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
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."

@input_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    book.data.pop(record.name.value)
    return "Contact removed."

@input_error
def add_email(args, book: AddressBook):
    name, email = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_email(email)
    return "Email added."

@input_error
def add_address(args, book: AddressBook):
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_address(address)
    return "Address added."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found")
    if record.birthday is None:
        return "Birthday not set."
    return f"{name}: {record.birthday}"

@input_error
def get_birthdays(args, book: AddressBook):
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the next {days} days."
    result = []
    for item in upcoming:
        result.append(
            f"{item['name']} -> {item['congratulation_date']}"
            )
    return "\n".join(result)

@input_error
def find_contact(args, book: AddressBook):
    query = " ".join(args)
    if not query:
        raise ValueError("Enter search query")
    results = book.search(query)
    if not results:
        return "No contacts found."
    return "\n\n".join(str(record) for record in results)