# TASK-4: Data Persistence (Disk Storage)

**Type:** Story  
**Priority:** High  
**Story Points:** 3  
**Epic:** Infrastructure  
**Suggested Assignee:** Dev 3  
**Dependencies:** TASK-2 (AddressBook model), TASK-3 (NoteBook model)

---

## Description

Implement serialization/deserialization for both `AddressBook` and `NoteBook` using the `pickle` protocol, stored in the user's home directory. Data must survive application restarts with zero loss.

---

## Technical Requirements

- Storage file location: `~/.personal_assistant/` (user home dir, hidden folder)
  - `addressbook.pkl`
  - `notebook.pkl`
- Use Python's `pickle` module for serialization
- Create the storage directory automatically if it does not exist

---

## Implementation in `storage/persistence.py`

```python
import pickle
from pathlib import Path

STORAGE_DIR = Path.home() / ".personal_assistant"

def _ensure_storage_dir():
    STORAGE_DIR.mkdir(exist_ok=True)

def save_data(obj, filename: str):
    _ensure_storage_dir()
    with open(STORAGE_DIR / filename, "wb") as f:
        pickle.dump(obj, f)

def load_data(filename: str, default_factory):
    path = STORAGE_DIR / filename
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default_factory()
```

Usage in `main.py`:
```python
book = load_data("addressbook.pkl", AddressBook)
notebook = load_data("notebook.pkl", NoteBook)

# ... main loop ...

save_data(book, "addressbook.pkl")
save_data(notebook, "notebook.pkl")
```

- `save_data` must be called on both `close` and `exit` commands
- `save_data` must also be called when the program exits due to `KeyboardInterrupt` (wrap main loop in try/finally)

---

## Acceptance Criteria

- [ ] `storage/persistence.py` implemented with `save_data` and `load_data`
- [ ] Storage directory `~/.personal_assistant/` created automatically on first run
- [ ] `AddressBook` is saved to `addressbook.pkl` on exit and loaded on startup
- [ ] `NoteBook` is saved to `notebook.pkl` on exit and loaded on startup
- [ ] If no `.pkl` file exists (first run), a fresh empty object is returned — no crash
- [ ] Data survives `close`, `exit` commands
- [ ] Data survives `Ctrl+C` (`KeyboardInterrupt`) — use try/finally in main loop
- [ ] No data files committed to Git (`.pkl` in `.gitignore`)
- [ ] Manual test: add a contact, exit, restart — contact is still present
- [ ] Manual test: add a note with tag, exit, restart — note and tag are still present

---

## Notes

- `pickle` preserves the full class structure including custom objects — no manual serialization needed
- If models change significantly (class refactor), old `.pkl` files may be incompatible — document this in README
