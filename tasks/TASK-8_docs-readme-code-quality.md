# TASK-8: README, Documentation & Code Quality

**Type:** Task  
**Priority:** Medium  
**Story Points:** 3  
**Epic:** Infrastructure  
**Suggested Assignee:** Dev 4 (or shared)  
**Dependencies:** TASK-5, TASK-6 (all commands finalized)

---

## Description

Finalize the project's public-facing documentation, ensure all code meets PEP 8 standards, add docstrings to all public classes and functions, and prepare the repository for mentor code review submission.

---

## README.md Requirements

The `README.md` must include:

1. **Project title and description** — what the app does (1–2 sentences)
2. **Requirements** — Python version (≥ 3.10), no external dependencies
3. **Installation**
   ```bash
   git clone <repo-url>
   cd personal_assistant
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Running the app**
   ```bash
   python main.py
   ```
5. **Full command reference table** — all commands with arguments and descriptions (same as `help` output)
6. **Data storage** — note that data is saved to `~/.personal_assistant/` automatically
7. **Examples** — 3–5 concrete usage examples showing add, find, notes, tags, birthdays

---

## Code Quality Requirements

### PEP 8
- [ ] All files pass `pycodestyle` or `flake8` with default settings (max line length 79 or configured to 99)
- [ ] No unused imports
- [ ] Consistent 4-space indentation throughout

### Docstrings
- [ ] All public classes have a one-line class docstring
- [ ] All public methods/functions have a docstring describing parameters and return value
- [ ] Example:
  ```python
  class AddressBook(UserDict):
      """Stores and manages contact records."""

      def find(self, name: str) -> Record | None:
          """Find a record by name (case-insensitive). Returns None if not found."""
  ```

### Inline Comments
- [ ] Non-obvious logic sections have brief inline comments (validation regex, birthday date shifting, etc.)

---

## Pre-submission Checklist

- [ ] `README.md` complete with all sections above
- [ ] All code passes `flake8` (run: `flake8 personal_assistant/`)
- [ ] No hardcoded paths (use `Path.home()` for storage)
- [ ] No `print` statements in model layer (`models/`) — only in handlers and `main.py`
- [ ] `.gitignore` covers `*.pkl`, `.venv/`, `__pycache__/`, `.idea/`
- [ ] Repository is public on GitHub/GitLab/Bitbucket
- [ ] Final commit message: `"Final project: Personal Assistant CLI"`
- [ ] All items in TECHNICAL_SPECIFICATIONS.md checklist manually verified as TRUE

---

## Manual Smoke Test Script

Before submission, run through this sequence manually:

```
python main.py
> add John 0501234567
> add-birthday John 15.06.1990
> add-email John john@example.com
> add-address John Kyiv, Khreshchatyk 1
> all
> find Joh
> birthdays 365
> add-note Shopping buy milk and bread
> add-tag 1 groceries
> show-notes
> find-by-tag groceries
> sort-by-tag groceries
> find-note milk
> edit-note 1 Shopping buy milk, bread and eggs
> show-note 1
> addd   (typo — check suggestion)
> help
> exit
python main.py
> all          (John should still be there)
> show-notes   (note should still be there)
> exit
```

---

## Notes

- This task can start in parallel once commands are stabilized (≈ TASK-5 + TASK-6 done)
- The mentor code review is a formal requirement — ensure repo is public and README is thorough
