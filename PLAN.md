# Python in 30 days

Budget: 30 minutes a day. Missing a day is fine: just pick up at the next one.

## How each day works

1. Read the day's `lesson.md` (about 5 minutes).
2. Solve the problems in the day's folder (about 20 minutes). Each problem file has
   checks at the bottom. Run the file; if it prints `All checks passed`, you're done.
3. Commit your work (about 2 minutes).

Short on time? Do problem 1 and stop. Extra time? Do the stretch problem.

Solutions are not in this folder. Ask me for "Day N solutions" after you've had a real go.

## Where you start

From your practice files, you can already:
- take input, use f-strings, if/elif/else, for loops
- write functions with parameters, work with lists and strings
- write simple classes and a tkinter window with try/except in it

Gaps this plan targets:
- Functions that `return` a value instead of printing inside (Day 1)
- Validating input: `float(input(...))` crashes on bad input (Day 2)
- Dictionaries and sets, which you haven't used yet (Days 5-6)
- Files, CSV, JSON, modules, tests, APIs (Weeks 2-4)

## The 30 days

| Day | Topic | Notes |
| --- | --- | --- |
| 1 | Functions that return a value | compute in the function, print outside |
| 2 | Input validation: try/except, while loops | fixes the calculator |
| 3 | Strings in depth: methods, slicing, formatting | |
| 4 | Lists in depth: methods, slicing, sorting with a key | |
| 5 | Dictionaries | |
| 6 | Tuples and sets, picking the right container | |
| 7 | Mini-project 1: command-line expense tracker | uses Days 1-6 |
| 8 | Reading and writing text files | `with`, `pathlib` |
| 9 | CSV files | |
| 10 | JSON files | |
| 11 | Modules, imports, splitting code across files | `if __name__ == "__main__"` |
| 12 | Errors in depth: reading tracebacks, raising your own | |
| 13 | Dates and times | |
| 14 | Mini-project 2: log file analyzer | homelab flavour |
| 15 | Classes: `__init__`, methods, `__repr__` | builds on Dog and Car |
| 16 | Objects working together (composition) | builds on Human |
| 17 | Inheritance, and when not to use it | |
| 18 | Testing: `assert` and pytest | |
| 19 | Debugging: print, pdb, Zed's debugger | |
| 20 | Comprehensions, `enumerate`, `zip`, `lambda` | |
| 21 | Mini-project 3: asset tracker class that saves to JSON | |
| 22 | Virtual environments and pip, properly | |
| 23 | HTTP and APIs with `requests` | |
| 24 | Command-line scripts with `argparse` | |
| 25 | Files and processes: `subprocess`, `shutil` | dry-run first |
| 26 | SQLite with `sqlite3` | |
| 27 | Regular expressions, the useful 20% | |
| 28-29 | Final project of your choice | |
| 30 | Review, read your own Pizza app with fresh eyes, plan the next 30 | |

The order can shift as we go. If something doesn't stick, we spend an extra day on it.
