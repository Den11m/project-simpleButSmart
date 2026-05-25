# TASK-2: Address Book — Data Models (OOP)

**Type:** Story  
**Priority:** High  
**Story Points:** 8  
**Epic:** Address Book  
**Suggested Assignee:** Dev 1  
**Dependencies:** TASK-1 (project structure)

---

## Description

Implement all OOP data models for the address book in `models/address_book.py`. This covers the full class hierarchy: `Field` → `Name`, `Phone`, `Email`, `Address`, `Birthday` → `Record` → `AddressBook`. Validation logic lives here, not in handlers.

---

## Class Specifications

### `Field` (base)
- `__init__(self, value)` stores `self.value`
- `__str__` returns `str(self.value)`

### `Name(Field)`
- Mandatory field; no empty string allowed (raise `ValueError` if blank)

### `Phone(Field)`
- Must be exactly **10 digits** (only digits, no spaces/dashes)
- Raise `ValueError("Phone must contain exactly 10 digits")` on invalid input

### `Email(Field)`
- Validate format: must contain `@` and a domain with a dot (e.g. `user@example.com`)
- Raise `ValueError("Invalid email format")` on invalid input
- Use `re` module for validation

### `Address(Field)`
- Free-text field, no special validation; just store the string

### `Birthday(Field)`
- Accept string in format `DD.MM.YYYY`
- Parse with `datetime.strptime(value, "%d.%m.%Y")`
- Raise `ValueError("Invalid date format. Use DD.MM.YYYY")` on failure
- Store as `datetime` object internally; `__str__` returns `DD.MM.YYYY`

### `Record`
```python
class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.emails: list[Email] = []
        self.address: Address | None = None
        self.birthday: Birthday | None = None
```
Methods required:
- `add_phone(phone: str)` — creates and appends `Phone` object
- `remove_phone(phone: str)` — removes by value; raise `ValueError` if not found
- `edit_phone(old: str, new: str)` — replaces old phone value; raise `ValueError` if old not found
- `find_phone(phone: str) -> Phone | None`
- `add_email(email: str)`
- `remove_email(email: str)`
- `edit_email(old: str, new: str)`
- `add_address(address: str)`
- `add_birthday(birthday: str)`
- `__str__` — readable multi-line representation of all fields

### `AddressBook(UserDict)`
- Inherits from `collections.UserDict`
- `add_record(record: Record)` — key = `record.name.value`
- `find(name: str) -> Record | None` — case-insensitive search; return `None` if not found
- `delete(name: str)` — raise `KeyError` if not found
- `search(query: str) -> list[Record]` — search across name, phones, emails (partial match, case-insensitive)
- `get_upcoming_birthdays(days: int = 7) -> list[dict]` — returns list of `{"name": ..., "congratulation_date": ...}` for contacts with birthdays within the next `days` days (if birthday falls on weekend, move congratulation to Monday)

---

## Acceptance Criteria

- [ ] All classes implemented in `models/address_book.py`
- [ ] `Phone` validation rejects non-10-digit strings and raises `ValueError`
- [ ] `Email` validation uses regex and raises `ValueError` on bad format
- [ ] `Birthday` validates date format and raises `ValueError` on bad input
- [ ] `Record` supports multiple phones and multiple emails
- [ ] `AddressBook.search()` returns matching records for partial name/phone/email query
- [ ] `AddressBook.get_upcoming_birthdays(days)` works correctly for arbitrary `days` parameter (not just 7)
- [ ] Weekend birthday shifting implemented (Sat/Sun → Monday)
- [ ] All classes have `__str__` or `__repr__` producing readable output
- [ ] Unit-testable: no side effects, no I/O in model layer

---

## Notes

- This task is on the critical path for TASK-5 (contact handlers) and TASK-4 (persistence)
- `search()` should support partial matching — needed for TASK-5's `find-contact` command
