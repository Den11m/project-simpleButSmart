# Personal Assistant CLI

A command-line personal assistant for managing contacts and notes.  
Stores contacts with phones, emails, addresses, and birthdays; manages text notes with tags — all persisted locally between sessions.

## Requirements

- Python **3.10** or higher
- No external runtime dependencies (stdlib only: `pickle`, `difflib`, `re`, `datetime`, `pathlib`)

## Installation

```bash
git clone <repo-url>
cd simple-but-smart
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

## Command Reference

### Contacts

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add` | `[name] [phone]` | Add a contact or append a phone to an existing one |
| `change` | `[name] [old_phone] [new_phone]` | Replace a phone number |
| `delete-contact` | `[name]` | Delete a contact |
| `phone` | `[name]` | Show all phone numbers for a contact |
| `all` | — | Show all contacts |
| `add-email` | `[name] [email]` | Add an email address to a contact |
| `add-address` | `[name] [address...]` | Set the address for a contact |
| `add-birthday` | `[name] [DD.MM.YYYY]` | Set the birthday for a contact |
| `show-birthday` | `[name]` | Show a contact's birthday |
| `birthdays` | `[days]` | List upcoming birthdays within N days (default 7) |
| `find` | `[query]` | Search contacts by name, phone, or email |

### Notes

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add-note` | `[title] [content...]` | Create a new note |
| `show-notes` | — | List all notes (summary view) |
| `show-note` | `[id]` | Show a single note in full |
| `find-note` | `[query]` | Search notes by title or content |
| `edit-note` | `[id] [title] [content...]` | Edit a note's title and content |
| `delete-note` | `[id]` | Delete a note |
| `add-tag` | `[id] [tag]` | Add a tag to a note |
| `remove-tag` | `[id] [tag]` | Remove a tag from a note |
| `find-by-tag` | `[tag]` | Find all notes with a given tag |
| `sort-by-tag` | `[tag]` | List notes — tagged first, then the rest |

### Other

| Command | Arguments | Description |
|---------|-----------|-------------|
| `hello` | — | Greet the assistant |
| `help` | — | Show the command reference |
| `close` / `exit` | — | Save data and exit |

## Data Storage

Data is saved automatically to `~/.personal_assistant/` on exit and loaded on startup — no data is lost between sessions.

```
~/.personal_assistant/
    addressbook.pkl
    notebook.pkl
```

> **Note:** pickle files are tied to the Python class structure. If model classes change, remove old files and restart:
> ```bash
> rm ~/.personal_assistant/*.pkl          # macOS / Linux
> Remove-Item "$HOME\.personal_assistant\*.pkl"   # Windows PowerShell
> ```

## Usage Examples

```
# Add a contact with phone, birthday, and email
> add John 0501234567
> add-birthday John 15.06.1990
> add-email John john@example.com
> add-address John Kyiv Khreshchatyk 1

# Search and view contacts
> find Joh
> all
> birthdays 365

# Work with notes
> add-note Shopping buy milk and bread
> add-tag 1 groceries
> show-notes
> find-by-tag groceries
> find-note milk
> edit-note 1 Shopping buy milk, bread and eggs
> show-note 1

# Fuzzy command suggestion
> addd
Unknown command 'addd'. Did you mean 'add'?

# Exit (data is persisted)
> exit
```
