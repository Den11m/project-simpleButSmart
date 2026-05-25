# Sprint Overview — Personal Assistant CLI

**Total Story Points:** 38  
**Team:** 3–4 developers  
**Goal:** Fully functional CLI personal assistant with contacts, notes, tags, persistence, and intelligent command suggestion

---

## Task Summary

| Task | Title | Points | Priority | Assignee Track | Dependencies |
|------|-------|--------|----------|----------------|--------------|
| TASK-1 | Project Setup & Architecture | 3 | High | Dev 1 | None |
| TASK-2 | Address Book — Data Models | 8 | High | Dev 1 | TASK-1 |
| TASK-3 | Notes — Data Models with Tags | 5 | High | Dev 2 | TASK-1 |
| TASK-4 | Data Persistence (pickle) | 3 | High | Dev 3 | TASK-2, TASK-3 |
| TASK-5 | Contacts — CLI Commands | 8 | High | Dev 1 | TASK-1, TASK-2 |
| TASK-6 | Notes — CLI Commands | 5 | High | Dev 2 | TASK-1, TASK-3 |
| TASK-7 | Intelligent Command Suggestion | 3 | Medium | Dev 3 | TASK-5, TASK-6 |
| TASK-8 | README, Docs & Code Quality | 3 | Medium | Dev 4 / shared | TASK-5, TASK-6 |

---

## Dependency Graph

```
TASK-1 ──┬──► TASK-2 ──► TASK-5 ──┬──► TASK-7
         │                        │
         └──► TASK-3 ──► TASK-6 ──┘
                    │         │
                    └────┬────┘
                         ▼
                      TASK-4
                         
TASK-5 + TASK-6 ──► TASK-8
```

---

## Suggested Developer Tracks

### 3-Developer Team

| Developer | Tasks (in order) |
|-----------|-----------------|
| **Dev 1** | TASK-1 → TASK-2 → TASK-5 |
| **Dev 2** | (wait for TASK-1) → TASK-3 → TASK-6 |
| **Dev 3** | (wait for TASK-2+3) → TASK-4 → TASK-7 → TASK-8 |

### 4-Developer Team

| Developer | Tasks (in order) |
|-----------|-----------------|
| **Dev 1** | TASK-1 → TASK-2 → TASK-5 |
| **Dev 2** | (wait for TASK-1) → TASK-3 → TASK-6 |
| **Dev 3** | (wait for TASK-2+3) → TASK-4 → TASK-7 |
| **Dev 4** | (wait for TASK-5+6) → TASK-8 + integration testing |

---

## Scoring Alignment

| Criteria | Covered by |
|---|---|
| Store contacts (name, address, phone, email, birthday) | TASK-2, TASK-5 |
| Upcoming birthdays in N days | TASK-2, TASK-5 |
| Phone & email validation | TASK-2 |
| Search contacts | TASK-2, TASK-5 |
| Edit & delete contacts | TASK-2, TASK-5 |
| Add text notes | TASK-3, TASK-6 |
| Search, edit, delete notes | TASK-3, TASK-6 |
| Data persistence (disk, no data loss) | TASK-4 |
| CLI interface, main loop, graceful exit | TASK-1, TASK-5 |
| Input error handling (no crashes) | TASK-1 (`@input_error`), all handlers |
| OOP, inheritance, composition | TASK-2, TASK-3 |
| PEP 8, comments, docstrings | TASK-8 |
| README with setup instructions | TASK-8 |
| Public GitHub repo | TASK-8 |
| **[+10] Tags for notes** | TASK-3, TASK-6 |
| **[+10] Search/sort notes by tags** | TASK-3, TASK-6 |
| **[bonus] Intelligent command suggestion** | TASK-7 |
