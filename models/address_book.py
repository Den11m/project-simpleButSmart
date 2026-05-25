"""Address book data models — stub. Implemented in TASK-2."""

from collections import UserDict


class Field:
    """Base class for contact record fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Mandatory contact name field."""
    pass


class Phone(Field):
    """Contact phone number field with validation (10 digits)."""
    pass


class Email(Field):
    """Contact email field with format validation."""
    pass


class Address(Field):
    """Free-text address field."""
    pass


class Birthday(Field):
    """Birthday field — accepts DD.MM.YYYY format."""
    pass


class Record:
    """Stores a single contact with name, phones, emails, address and birthday."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None


class AddressBook(UserDict):
    """Stores and manages contact Records, keyed by name."""
    pass
