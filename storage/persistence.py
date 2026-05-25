"""Disk persistence for AddressBook and NoteBook via pickle."""

import pickle
from pathlib import Path

STORAGE_DIR = Path.home() / ".personal_assistant"


def _ensure_storage_dir() -> None:
    """Create the storage directory if it does not exist."""
    STORAGE_DIR.mkdir(exist_ok=True)


def save_data(obj, filename: str) -> None:
    """Serialize obj to STORAGE_DIR/filename using pickle."""
    _ensure_storage_dir()
    with open(STORAGE_DIR / filename, "wb") as f:
        pickle.dump(obj, f)


def load_data(filename: str, default_factory):
    """Deserialize object from STORAGE_DIR/filename.

    Returns default_factory() if the file does not exist yet.
    """
    path = STORAGE_DIR / filename
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default_factory()
