"""Notes data models: Tag, Note, NoteBook.

Pure data layer — no I/O, no CLI coupling. Tags are normalized to lowercase
so equality, hashing, and search are case-insensitive.
"""

from datetime import datetime


class Tag:
    """A normalized keyword tag for a Note."""

    def __init__(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tag cannot be empty")
        # Strip any leading '#' so Tag('#work') and Tag('work') are equal,
        # and str(Tag('#work')) is '#work' rather than '##work'.
        normalized = value.strip().lower().lstrip("#").strip()
        if not normalized:
            raise ValueError("Tag cannot be empty")
        self.value = normalized

    def __str__(self):
        return f"#{self.value}"

    def __repr__(self):
        return f"Tag({self.value!r})"

    def __eq__(self, other):
        return isinstance(other, Tag) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Note:
    """A text note with optional tags and creation/update timestamps."""

    def __init__(self, title: str, content: str):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty")
        if not isinstance(content, str):
            raise ValueError("Content must be a string")
        self.id: int | None = None
        self.title: str = title.strip()
        self.content: str = content
        self.tags: list[Tag] = []
        now = datetime.now()
        self.created_at: datetime = now
        self.updated_at: datetime = now

    def add_tag(self, tag: str) -> None:
        """Add a tag; silently ignore if it already exists on this note."""
        new_tag = Tag(tag)
        if new_tag not in self.tags:
            self.tags.append(new_tag)
            self.updated_at = datetime.now()

    def remove_tag(self, tag: str) -> None:
        """Remove a tag by value. Raises ValueError if the tag is not present."""
        target = Tag(tag)
        if target not in self.tags:
            raise ValueError(f"Tag '{target}' not found on this note")
        self.tags.remove(target)
        self.updated_at = datetime.now()

    def edit(self, title: str | None = None, content: str | None = None) -> None:
        """Update title and/or content. Refreshes updated_at only if a value actually changed."""
        if title is None and content is None:
            return
        changed = False
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Title cannot be empty")
            new_title = title.strip()
            if new_title != self.title:
                self.title = new_title
                changed = True
        if content is not None:
            if not isinstance(content, str):
                raise ValueError("Content must be a string")
            if content != self.content:
                self.content = content
                changed = True
        if changed:
            self.updated_at = datetime.now()

    def has_tag(self, tag: str) -> bool:
        """Case-insensitive check for tag membership."""
        try:
            return Tag(tag) in self.tags
        except ValueError:
            return False

    def __str__(self):
        tags = ", ".join(str(t) for t in self.tags) if self.tags else "—"
        return (
            f"[#{self.id}] {self.title}\n"
            f"Tags    : {tags}\n"
            f"Content : {self.content}\n"
            f"Created : {self.created_at.strftime('%Y-%m-%d %H:%M')}\n"
            f"Updated : {self.updated_at.strftime('%Y-%m-%d %H:%M')}"
        )


class NoteBook:
    """Stores and manages Note objects with search and tag-based filtering."""

    def __init__(self):
        self._notes: list[Note] = []
        self._next_id: int = 1

    def add(self, title: str, content: str) -> Note:
        """Create a new note with an auto-incremented id and store it."""
        note = Note(title, content)
        note.id = self._next_id
        self._next_id += 1
        self._notes.append(note)
        return note

    def find_by_id(self, note_id: int) -> Note | None:
        """Return the note with the given id, or None."""
        return next((n for n in self._notes if n.id == note_id), None)

    def delete(self, note_id: int) -> None:
        """Remove a note by id. Raises ValueError if not found."""
        note = self.find_by_id(note_id)
        if note is None:
            raise ValueError(f"Note with id {note_id} not found")
        self._notes.remove(note)

    def search(self, query: str) -> list[Note]:
        """Case-insensitive partial match against title or content."""
        q = query.strip().lower()
        if not q:
            return []
        return [
            n for n in self._notes
            if q in n.title.lower() or q in n.content.lower()
        ]

    def find_by_tag(self, tag: str) -> list[Note]:
        """Return all notes carrying the given tag."""
        return [n for n in self._notes if n.has_tag(tag)]

    def all(self) -> list[Note]:
        """Return a shallow copy of all notes, in insertion order."""
        return list(self._notes)

    def sort_by_tag(self, tag: str) -> list[Note]:
        """Return notes with the tag first, untagged-by-this-tag after. Stable within groups."""
        tagged = [n for n in self._notes if n.has_tag(tag)]
        rest = [n for n in self._notes if not n.has_tag(tag)]
        return tagged + rest

    def __len__(self):
        return len(self._notes)

    def __iter__(self):
        return iter(self._notes)

    def __str__(self):
        if not self._notes:
            return "NoteBook is empty."
        return "\n\n".join(str(n) for n in self._notes)
