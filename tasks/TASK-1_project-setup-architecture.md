# TASK-1: Project Setup & Architecture

**Type:** Task  
**Priority:** High  
**Story Points:** 3  
**Epic:** Infrastructure  
**Suggested Assignee:** Dev 1  
**Dependencies:** None — start immediately

---

## Description

Initialize the project repository and establish the shared architectural foundation that all other tasks depend on. This includes the directory structure, virtual environment, base module skeleton, shared utilities (error-handling decorator, `parse_input`), and CI-friendly configuration.

---

## Acceptance Criteria

- [ ] Public GitHub repository created (or GitLab/Bitbucket)
- [ ] `.gitignore` includes `__pycache__`, `.venv/`, `*.pkl`, `.idea/`
- [ ] `requirements.txt` with all dependencies and versions (at minimum: Python ≥ 3.10)
- [ ] Project package structure established:
  ```
  personal_assistant/
  ├── main.py               # entry point
  ├── models/
  │   ├── __init__.py
  │   ├── address_book.py   # stub
  │   └── notes.py          # stub
  ├── handlers/
  │   ├── __init__.py
  │   ├── contact_handlers.py  # stub
  │   └── note_handlers.py     # stub
  ├── utils/
  │   ├── __init__.py
  │   ├── decorators.py     # @input_error decorator
  │   └── parser.py         # parse_input function
  └── storage/
      ├── __init__.py
      └── persistence.py    # stub
  ```
- [ ] `parse_input(user_input)` implemented in `utils/parser.py` — splits raw input into `(command, *args)`, lowercases command, strips whitespace
- [ ] `@input_error` decorator implemented in `utils/decorators.py` — catches `KeyError`, `ValueError`, `IndexError` and returns a user-friendly string (no crash)
- [ ] `main.py` contains the main event loop skeleton (while True, command dispatch, `close`/`exit` breaks gracefully)
- [ ] App can be launched with `python main.py` without errors (even with stubs)
- [ ] Basic `README.md` with project title and "Installation" section placeholder

---

## Notes

- The `@input_error` decorator is critical for all handler tasks (TASK-5, TASK-6) — deliver it early
- Keep `main.py` as a thin dispatcher; all logic lives in handlers/models
