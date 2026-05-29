# Personal Assistant CLI

A command-line personal assistant for managing contacts and notes, built with Python.

## Requirements

- Python 3.10 or higher
- No external runtime dependencies (stdlib only)

## Installation

```bash
git clone <repo-url>
cd personal_assistant
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

## Data Storage

All data is automatically saved to `~/.personal_assistant/` on exit and restored on next startup. No data is lost between sessions.

## Command Reference

Full command list is available inside the app via the `help` command.

---

*See `tasks/` directory for the project task breakdown.*



## Data Storage Notes

Application data is stored locally in the user's home directory:

```text
~/.personal_assistant/
```

The application uses pickle files for persistence:

```text
addressbook.pkl
notebook.pkl
```

Because pickle preserves the Python class structure, changes to model classes such as `AddressBook`, `NoteBook`, `Record`, or `Note` may make older `.pkl` files incompatible.

If the app crashes after model refactoring, remove the old saved pickle files and restart the app:

```bash
rm ~/.personal_assistant/*.pkl
```

On Windows PowerShell:

```powershell
Remove-Item "$HOME\.personal_assistant\*.pkl"
```
