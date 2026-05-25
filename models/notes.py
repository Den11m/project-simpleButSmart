"""Notes data models — stub. Implemented in TASK-3."""


class Tag:
    """A normalized keyword tag for a Note."""
    pass


class Note:
    """A text note with optional tags, timestamps, and auto-assigned ID."""
    pass


class NoteBook:
    """Stores and manages Note objects with search and tag-based filtering."""

    def __init__(self):
        self._notes = []
        self._next_id = 1
