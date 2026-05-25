# TASK-5: Contacts — CLI Commands & Handlers

**Type:** Story  
**Priority:** High  
**Story Points:** 8  
**Epic:** Address Book  
**Suggested Assignee:** Dev 1  
**Dependencies:** TASK-1 (decorators, parser), TASK-2 (AddressBook models)

---

## Description

Implement all CLI command handler functions for contact management in `handlers/contact_handlers.py` and wire them into `main.py`. All handlers must use the `@input_error` decorator. Output must be readable and user-friendly.

---

## Commands to Implement

| Command | Arguments | Description |
|---|---|---|
| `add` | `[name] [phone]` | Add new contact or add phone to existing contact |
| `change` | `[name] [old_phone] [new_phone]` | Edit phone number for a contact |
| `delete-contact` | `[name]` | Delete a contact entirely |
| `phone` | `[name]` | Show all phones for a contact |
| `add-email` | `[name] [email]` | Add email to a contact |
| `add-address` | `[name] [address...]` | Add address to a contact (multi-word) |
| `add-birthday` | `[name] [DD.MM.YYYY]` | Add birthday to a contact |
| `show-birthday` | `[name]` | Show birthday of a contact |
| `birthdays` | `[days]` (optional, default 7) | Show contacts with upcoming birthdays within N days |
| `find` | `[query]` | Search contacts by name, phone, or email (partial match) |
| `all` | — | Show all contacts in address book |

---

## Handler Signatures

All functions in `handlers/contact_handlers.py`:

```python
@input_error
def add_contact(args: list[str], book: AddressBook) -> str: ...

@input_error
def change_phone(args: list[str], book: AddressBook) -> str: ...

@input_error
def delete_contact(args: list[str], book: AddressBook) -> str: ...

@input_error
def show_phone(args: list[str], book: AddressBook) -> str: ...

@input_error
def add_email(args: list[str], book: AddressBook) -> str: ...

@input_error
def add_address(args: list[str], book: AddressBook) -> str: ...

@input_error
def add_birthday(args: list[str], book: AddressBook) -> str: ...

@input_error
def show_birthday(args: list[str], book: AddressBook) -> str: ...

@input_error
def get_birthdays(args: list[str], book: AddressBook) -> str: ...

@input_error
def find_contact(args: list[str], book: AddressBook) -> str: ...

@input_error
def show_all(args: list[str], book: AddressBook) -> str: ...
```

---

## CLI UX Requirements

- Main menu (list of commands) shown **only once** at startup — not after every command
- `find` with no results returns `"No contacts found."` — not an error
- `all` with empty book returns `"Address book is empty."` — not an error
- `birthdays` with no upcoming birthdays returns `"No birthdays in the next N days."` — not an error
- Phone/email validation errors from the model layer are caught by `@input_error` and printed as messages — program continues
- Commands must be **case-insensitive** (`ADD` = `add`)
- Multi-word address support: `add-address John 123 Main Street` → address = `"123 Main Street"`

---

## Acceptance Criteria

- [ ] All 11 commands implemented and wired in `main.py`
- [ ] `add` creates a new contact if name not found; adds phone to existing if name found
- [ ] `change` updates phone and returns `"Phone updated."` or error if old phone not found
- [ ] `delete-contact` removes the contact and confirms deletion
- [ ] `find` returns formatted list of all matching contacts (name, phones, emails, birthday)
- [ ] `all` returns all contacts in a readable table/list format
- [ ] `birthdays [days]` accepts optional number of days (default 7); works with any value
- [ ] Invalid phone format → error message printed, program continues
- [ ] Invalid email format → error message printed, program continues
- [ ] Invalid date format → error message printed, program continues
- [ ] Missing arguments → error message printed, program continues
- [ ] Non-existent contact → error message printed, program continues
- [ ] Commands are case-insensitive

---

## Notes

- Handler functions return **strings** (not print directly) — `main.py` does `print(handler(...))`
- This makes handlers unit-testable without mocking stdout
