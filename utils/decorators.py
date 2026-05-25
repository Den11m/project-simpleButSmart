"""Shared decorators for CLI handler functions."""


def input_error(func):
    """Catch KeyError, ValueError, IndexError and return a user-friendly message instead of crashing."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Contact not found: {e}"
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments provided."
    return inner
