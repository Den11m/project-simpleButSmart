"""CLI handler functions for note management.

Each handler takes (args: list[str], notebook: NoteBook) and returns a string;
main.py prints the result. The @input_error decorator turns model-layer
ValueErrors (invalid tag, missing note, etc.) into friendly messages so the
CLI loop never crashes on bad input.
"""

from utils.decorators import input_error
from models.notes import NoteBook, Tag

CONTENT_PREVIEW_LEN = 50


def _parse_id(raw: str) -> int:
    """Convert a CLI token to a note id, with a friendly error for non-integers."""
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"Invalid note ID: '{raw}'. ID must be a whole number.")


def _require_note(notebook: NoteBook, note_id: int):
    """Return the note with the given id or raise a friendly ValueError."""
    note = notebook.find_by_id(note_id)
    if note is None:
        raise ValueError(f"Note with id {note_id} not found.")
    return note


def _format_summary(note) -> str:
    """One-line list view: [ID] Title | Tags: #t1 #t2 | content preview..."""
    tags = " ".join(str(t) for t in note.tags) if note.tags else "—"
    content = note.content.replace("\n", " ")
    if len(content) > CONTENT_PREVIEW_LEN:
        content = content[:CONTENT_PREVIEW_LEN].rstrip() + "..."
    return f"[{note.id}] {note.title} | Tags: {tags} | {content}"


@input_error
def add_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: add-note [title] [content...]")
    title = args[0]
    content = " ".join(args[1:])
    note = notebook.add(title, content)
    return f"Note added with ID: {note.id}"


@input_error
def show_all_notes(args: list[str], notebook: NoteBook) -> str:
    notes = notebook.all()
    if not notes:
        return "No notes yet."
    return "\n".join(_format_summary(n) for n in notes)


@input_error
def show_note(args: list[str], notebook: NoteBook) -> str:
    if not args:
        raise ValueError("Usage: show-note [id]")
    note = _require_note(notebook, _parse_id(args[0]))
    return str(note)


@input_error
def find_note(args: list[str], notebook: NoteBook) -> str:
    if not args:
        raise ValueError("Usage: find-note [query]")
    query = " ".join(args)
    results = notebook.search(query)
    if not results:
        return f"No notes matching '{query}'."
    return "\n".join(_format_summary(n) for n in results)


@input_error
def edit_note(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 3:
        raise ValueError("Usage: edit-note [id] [title] [content...]")
    note_id = _parse_id(args[0])
    note = _require_note(notebook, note_id)
    note.edit(title=args[1], content=" ".join(args[2:]))
    return f"Note {note_id} updated."


@input_error
def delete_note(args: list[str], notebook: NoteBook) -> str:
    if not args:
        raise ValueError("Usage: delete-note [id]")
    note_id = _parse_id(args[0])
    notebook.delete(note_id)
    return f"Note {note_id} deleted."


@input_error
def add_tag(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: add-tag [id] [tag]")
    note_id = _parse_id(args[0])
    note = _require_note(notebook, note_id)
    note.add_tag(args[1])
    return f"Tag {Tag(args[1])} added to note {note_id}."


@input_error
def remove_tag(args: list[str], notebook: NoteBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: remove-tag [id] [tag]")
    note_id = _parse_id(args[0])
    note = _require_note(notebook, note_id)
    note.remove_tag(args[1])
    return f"Tag {Tag(args[1])} removed from note {note_id}."


@input_error
def find_by_tag(args: list[str], notebook: NoteBook) -> str:
    if not args:
        raise ValueError("Usage: find-by-tag [tag]")
    results = notebook.find_by_tag(args[0])
    if not results:
        return f"No notes with tag '{Tag(args[0])}'."
    return "\n".join(_format_summary(n) for n in results)


@input_error
def sort_by_tag(args: list[str], notebook: NoteBook) -> str:
    if not args:
        raise ValueError("Usage: sort-by-tag [tag]")
    notes = notebook.sort_by_tag(args[0])
    if not notes:
        return "No notes yet."
    return "\n".join(_format_summary(n) for n in notes)
