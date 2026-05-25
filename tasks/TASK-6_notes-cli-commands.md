# TASK-6: Notes — CLI Commands & Handlers

**Type:** Story  
**Priority:** High  
**Story Points:** 5  
**Epic:** Notes  
**Suggested Assignee:** Dev 2  
**Dependencies:** TASK-1 (decorators, parser), TASK-3 (NoteBook models)

---

## Description

Implement all CLI command handler functions for note management in `handlers/note_handlers.py` and wire them into `main.py`. Includes tag management commands (additional requirements). All handlers must use the `@input_error` decorator. Output must be readable and user-friendly.

---

## Commands to Implement

| Command | Arguments | Description |
|---|---|---|
| `add-note` | `[title] [content...]` | Create a new note (content may be multi-word) |
| `show-notes` | — | Show all notes |
| `show-note` | `[id]` | Show a single note by ID |
| `find-note` | `[query]` | Search notes by title or content (partial match) |
| `edit-note` | `[id] [title] [content...]` | Edit existing note's title and/or content |
| `delete-note` | `[id]` | Delete a note by ID |
| `add-tag` | `[id] [tag]` | Add a tag to a note |
| `remove-tag` | `[id] [tag]` | Remove a tag from a note |
| `find-by-tag` | `[tag]` | Find all notes with the given tag |
| `sort-by-tag` | `[tag]` | Show notes sorted: matching tag first, rest after |

---

## Handler Signatures

All functions in `handlers/note_handlers.py`:

```python
@input_error
def add_note(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def show_all_notes(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def show_note(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def find_note(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def edit_note(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def delete_note(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def add_tag(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def remove_tag(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def find_by_tag(args: list[str], notebook: NoteBook) -> str: ...

@input_error
def sort_by_tag(args: list[str], notebook: NoteBook) -> str: ...
```

---

## Argument Parsing Notes

- `add-note` first token after command = title, remaining tokens = content joined with spaces
  - e.g. `add-note Shopping buy milk and eggs` → title=`"Shopping"`, content=`"buy milk and eggs"`
- `edit-note` first token = id (int), second = new title, remaining = new content joined with spaces
- `add-tag` / `remove-tag`: first token = note id (int), second = tag string

---

## CLI UX Requirements

- `show-notes` with empty notebook returns `"No notes yet."` — not an error
- `find-note` with no results returns `"No notes matching '[query]'."` — not an error
- `find-by-tag` with no results returns `"No notes with tag '#[tag]'."` — not an error
- Note output format shows: `[ID] Title | Tags: #tag1 #tag2 | Content...` (truncated if long) or full detail for `show-note`
- Timestamps (`created_at`) shown in `show-note` detail view

---

## Acceptance Criteria

- [ ] All 10 commands implemented and wired in `main.py`
- [ ] `add-note` creates note and returns `"Note added with ID: N"`
- [ ] `show-notes` lists all notes with IDs, titles, and tags
- [ ] `show-note [id]` shows full note including content, tags, created/updated timestamps
- [ ] `find-note` performs partial case-insensitive search on title and content
- [ ] `edit-note` updates note and returns `"Note N updated."`
- [ ] `delete-note` removes note and returns `"Note N deleted."`
- [ ] `add-tag` adds tag to note and returns `"Tag #tag added to note N."`
- [ ] `remove-tag` removes tag from note and returns `"Tag #tag removed from note N."`
- [ ] `find-by-tag` returns all notes that have the given tag
- [ ] `sort-by-tag` returns notes with given tag first, then remaining notes
- [ ] Invalid note ID (non-integer or not found) → error message, program continues
- [ ] Missing arguments → error message, program continues

---

## Notes

- Handler functions return **strings** — `main.py` does `print(handler(...))`
- Tags are normalized to lowercase in the model layer (TASK-3); handlers just pass the string
- Both `find-by-tag` and `sort-by-tag` are needed for the +10 additional score
