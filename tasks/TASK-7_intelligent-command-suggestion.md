# TASK-7: Intelligent Command Suggestion (Fuzzy Matching)

**Type:** Story  
**Priority:** Medium  
**Story Points:** 3  
**Epic:** CLI UX  
**Suggested Assignee:** Dev 3  
**Dependencies:** TASK-5 (full command list from contacts), TASK-6 (full command list from notes)

---

## Description

When a user enters an unrecognized command, the assistant should intelligently suggest the closest valid command instead of just printing `"Invalid command."`. This satisfies the "Помічник повинен вгадувати, що хоче від нього користувач" criterion.

---

## Technical Approach

Use Python's built-in `difflib.get_close_matches` — no third-party dependencies required.

```python
from difflib import get_close_matches

ALL_COMMANDS = [
    "add", "change", "delete-contact", "phone", "add-email",
    "add-address", "add-birthday", "show-birthday", "birthdays",
    "find", "all", "add-note", "show-notes", "show-note",
    "find-note", "edit-note", "delete-note", "add-tag",
    "remove-tag", "find-by-tag", "sort-by-tag", "hello",
    "close", "exit", "help",
]

def suggest_command(user_input: str) -> str | None:
    matches = get_close_matches(user_input.lower(), ALL_COMMANDS, n=1, cutoff=0.6)
    return matches[0] if matches else None
```

---

## Integration in `main.py`

Replace the `else: print("Invalid command.")` branch with:

```python
else:
    suggestion = suggest_command(command)
    if suggestion:
        print(f"Unknown command '{command}'. Did you mean '{suggestion}'?")
    else:
        print(f"Unknown command '{command}'. Type 'help' to see available commands.")
```

---

## `help` Command

Add a `help` command that prints a formatted table of all available commands with brief descriptions:

```
Available commands:
  add [name] [phone]              - Add contact or add phone to existing
  change [name] [old] [new]       - Change phone number
  ...
```

---

## Acceptance Criteria

- [ ] `suggest_command()` implemented in `utils/parser.py` or a new `utils/suggestions.py`
- [ ] `ALL_COMMANDS` list contains all commands from TASK-5 and TASK-6
- [ ] Typo in command (e.g., `addd`, `phon`, `bithdays`) → suggestion printed, program continues
- [ ] Completely unrelated input → `"Unknown command. Type 'help' to see available commands."`
- [ ] `help` command implemented and wired in `main.py` — shows all commands with short descriptions
- [ ] Suggestion uses `cutoff=0.6` (tune if needed, but ≥ 0.5)
- [ ] No third-party packages required (use `difflib` from stdlib)

---

## Notes

- `difflib.get_close_matches` uses SequenceMatcher internally — works well for short command names
- Keep `ALL_COMMANDS` as a single source of truth (one list, not scattered)
- This feature is explicitly listed in the checklist and earns points — don't skip it
