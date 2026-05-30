"""Address book data models — implemented in TASK-2."""

import re
from collections import UserDict
from datetime import datetime, timedelta


class Field:
    """Base class for contact record fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Mandatory contact name field."""

    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value.strip())


class Phone(Field):
    """Contact phone number field with validation (10 digits)."""

    def __init__(self, value: str):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone must contain exactly 10 digits")
        super().__init__(value)


class Email(Field):
    """Contact email field with format validation."""

    def __init__(self, value: str):
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
            raise ValueError("Invalid email format")
        super().__init__(value)


class Address(Field):
    """Free-text address field."""


class Birthday(Field):
    """Birthday field — accepts DD.MM.YYYY format."""

    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    """Stores a single contact with name, phones, emails, address and birthday."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.emails: list[Email] = []
        self.address: Address | None = None
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str) -> None:
        """Validate and append a phone number to this record."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """Remove a phone number. Raises ValueError if not present."""
        target = self.find_phone(phone)
        if target is None:
            raise ValueError(f"Phone {phone} not found")
        self.phones.remove(target)

    def edit_phone(self, old: str, new: str) -> None:
        """Replace old phone with new. Raises ValueError if old not found."""
        target = self.find_phone(old)
        if target is None:
            raise ValueError(f"Phone {old} not found")
        idx = self.phones.index(target)
        self.phones[idx] = Phone(new)

    def find_phone(self, phone: str) -> Phone | None:
        """Return the Phone object matching value, or None."""
        return next((p for p in self.phones if p.value == phone), None)

    def add_email(self, email: str) -> None:
        """Validate and append an email address to this record."""
        self.emails.append(Email(email))

    def remove_email(self, email: str) -> None:
        """Remove an email address. Raises ValueError if not present."""
        target = next((e for e in self.emails if e.value == email), None)
        if target is None:
            raise ValueError(f"Email {email} not found")
        self.emails.remove(target)

    def edit_email(self, old: str, new: str) -> None:
        """Replace old email with new. Raises ValueError if old not found."""
        target = next((e for e in self.emails if e.value == old), None)
        if target is None:
            raise ValueError(f"Email {old} not found")
        idx = self.emails.index(target)
        self.emails[idx] = Email(new)

    def add_address(self, address: str) -> None:
        """Set (or replace) the free-text address for this record."""
        self.address = Address(address)

    def add_birthday(self, birthday: str) -> None:
        """Set (or replace) the birthday (DD.MM.YYYY) for this record."""
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = ", ".join(str(p) for p in self.phones) or "—"
        emails = ", ".join(str(e) for e in self.emails) or "—"
        address = str(self.address) if self.address else "—"
        birthday = str(self.birthday) if self.birthday else "—"
        return (
            f"Name    : {self.name}\n"
            f"Phones  : {phones}\n"
            f"Emails  : {emails}\n"
            f"Address : {address}\n"
            f"Birthday: {birthday}"
        )


class AddressBook(UserDict):
    """Stores and manages contact Records, keyed by name."""

    def add_record(self, record: Record) -> None:
        """Store a Record, keyed by its name value."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name (case-insensitive). Returns None if not found."""
        name_lower = name.lower()
        return next(
            (r for k, r in self.data.items() if k.lower() == name_lower), None
        )

    def delete(self, name: str) -> None:
        """Delete a record by name. Raises KeyError if not found."""
        record = self.find(name)
        if record is None:
            raise KeyError(f"Contact '{name}' not found")
        del self.data[record.name.value]

    def search(self, query: str) -> list[Record]:
        """Case-insensitive partial match against name, phones, and emails."""
        q = query.lower()
        results = []
        for record in self.data.values():
            if (
                q in record.name.value.lower()
                or any(q in p.value for p in record.phones)
                or any(q in e.value.lower() for e in record.emails)
            ):
                results.append(record)
        return results

    def get_upcoming_birthdays(self, days: int = 7) -> list[dict]:
        """Return contacts with birthdays in the next `days` days.

        Each entry is {'name': str, 'congratulation_date': 'DD.MM.YYYY'}.
        Birthdays falling on Saturday/Sunday are shifted to Monday.
        """
        today = datetime.today().date()
        upcoming = []
        for record in self.data.values():
            if record.birthday is None:
                continue
            bday = record.birthday.value.date()
            # Project birthday to the current year for comparison
            bday_this_year = bday.replace(year=today.year)
            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)
            delta = (bday_this_year - today).days
            if 0 <= delta <= days:
                congrats = bday_this_year
                # Shift weekend congratulation dates to Monday
                if congrats.weekday() == 5:  # Saturday
                    congrats += timedelta(days=2)
                elif congrats.weekday() == 6:  # Sunday
                    congrats += timedelta(days=1)
                upcoming.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congrats.strftime("%d.%m.%Y"),
                    }
                )
        return upcoming
