# python-learning

Working repository for a career transition into Python development.
Exercises, notes, and — as the plan progresses — deployed projects.

Written by **Vladimir Marković**. Background in environmental and sustainable
development engineering; moving into backend development, with a deliberate
focus on where those two overlap (utilities, energy, environmental monitoring,
regulatory reporting).

This is a learning repository, not a portfolio of finished work. It is public
on purpose: the commit history is the record of how the learning actually went,
including the bugs and the things that took two attempts.

## Contents

| File | What it covers |
|---|---|
| `temperature_converter.py` | Functions, input validation, raising exceptions, docstrings |
| `string_analyzer.py` | Dictionary counting pattern, `max(d, key=d.get)`, empty-input guards |
| `contact_book.py` | First class: CRUD over a dict, `__str__`, reverse lookup |
| `grade_calculator.py` | Function composition, list comprehensions, guard clauses |
| `expense_tracker.py` | List-of-dicts design, `lambda` in `max(key=...)`, generator expressions |
| `bank_accounts.py` | Inheritance, `super().__init__()`, method overriding |
| `handoff.md` | The study plan, and the reasoning behind it |

## Running

Python 3.11.7 via pyenv. No third-party dependencies yet.

```bash
python temperature_converter.py
```

Each file runs standalone. Everything below `if __name__ == "__main__":` is a
set of hand-written checks that print expected versus actual — a stand-in for
real tests, which arrive in the next milestone.

## What's next

Working through a milestone-based plan (`handoff.md`), in order:

- **M1** — pytest, retrofitting real tests onto everything above
- **M2** — SQL and PostgreSQL; porting the expense tracker to a database
- **M3** — a deployed FastAPI service, documented down to its failure modes
- **M4** — a project in the environmental/utilities domain

## A note on the commit history

Commit messages here record known problems as well as fixes — for example,
`temperature_converter.py` currently reports "not a number" and "unrecognised
unit" through the same `ValueError`, which is written down rather than quietly
patched. Those get resolved when the tests arrive in M1.

The intent is that the log reads as an honest record of the work, rather than
a tidy fiction assembled afterwards.
