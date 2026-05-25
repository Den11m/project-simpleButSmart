# TASK-3: Notes — Data Models with Tags (OOP)

**Type:** Story  
**Priority:** High  
**Story Points:** 5  
**Epic:** Notes  
**Suggested Assignee:** Dev 2  
**Dependencies:** TASK-1 (project structure)

---

## Description

Implement all OOP data models for the notes system in `models/notes.py`. This covers `Tag`, `Note`, and `NoteBook`. Tags are a required additional feature (+10 points). The model layer must be pure logic — no I/O, no CLI coupling.

---

## Class Specifications

### `Tag`
```python
class Tag:
    def __init__(self, value: str):
        self.value = value.strip().lower()  # normalize on creation

    def __str__(self):
        return f"#{self.value}"

    def __eq__(self, other):
        return isinstance(other, Tag) and self.value == other.value

    def __hash__(self):
        return hash(self.value)
```

### `Note`
```python
class Note:
    def __init__(self, title: str, content: str):
        self.id: int          # auto-assigned by NoteBook
        self.title: str
        self.content: str
        self.tags: list[Tag] = []
        self.created_at: datetime
        self.updated_at: datetime
```
Methods required:
- `add_tag(tag: str)` — creates `Tag` object, appends if not already present
- `remove_tag(tag: str)` — removes by value; raise `ValueError` if not found
- `edit(title: str | None = None, content: str | None = None)` — update provided fields, refresh `updated_at`
- `has_tag(tag: str) -> bool` — case-insensitive check
- `__str__` — human-readable output showing id, title, tags, content

### `NoteBook`
```python
class NoteBook:
    def __init__(self):
        self._notes: list[Note] = []
        self._next_id: int = 1
```
Methods required:
- `add(title: str, content: str) -> Note` — creates note with auto-incremented id, appends to list, returns the note
- `find_by_id(note_id: int) -> Note | None`
- `delete(note_id: int)` — raise `ValueError` if not found
- `search(query: str) -> list[Note]` — case-insensitive partial match on title AND content
- `find_by_tag(tag: str) -> list[Note]` — returns notes that have the given tag
- `all() -> list[Note]` — returns all notes (copy of list)
- `sort_by_tag(tag: str) -> list[Note]` — notes matching the tag first, rest after; stable order within groups

---

## Acceptance Criteria

- [ ] All classes implemented in `models/notes.py`
- [ ] `Tag` normalizes to lowercase, supports equality and hashing
- [ ] `Note` stores `created_at` / `updated_at` timestamps (auto-set)
- [ ] Duplicate tags are silently ignored in `add_tag`
- [ ] `NoteBook.add()` auto-increments IDs starting from 1
- [ ] `NoteBook.search()` matches partial title or content, case-insensitive
- [ ] `NoteBook.find_by_tag()` returns correct subset
- [ ] `NoteBook.sort_by_tag()` returns tagged notes first, untagged after
- [ ] All classes have `__str__` producing readable output
- [ ] No I/O or CLI logic in model layer — purely data manipulation

---

## Notes

- This task is parallel to TASK-2; both can start after TASK-1
- Tags feature is required for the additional 10 points — implement fully, not as an afterthought
- `NoteBook` does **not** inherit `UserDict`; use a plain list internally
