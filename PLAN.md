# Python in 35 sessions

Budget: about 30 minutes a session. Some sessions will take longer, and that's fine.

"Day N" below means the Nth session, not the Nth calendar day. Take a day off whenever you
like, and if a lesson needs two sittings, take two. Understanding matters more than speed.
35 sessions is a ceiling, not a target: if we finish sooner, the extra time goes to a
bigger final project.

## How a normal session works

1. Read the day's `lesson.md` (about 5 minutes).
2. Solve the problems in the day's folder (about 20 minutes). Each problem file has
   checks at the bottom. Run the file; if it prints `All checks passed`, you're done.
3. Commit your work (about 2 minutes), with a message that says what changed.

Short on time? Do problem 1 and stop. Extra time? Do the stretch problem.

Solutions are not in this folder. Ask me for "Day N solutions" after you've had a real go.

## Checkpoint days (every 4th session)

After every three lesson days there is a checkpoint instead of a new lesson. It's a
30-minute closed-book quiz of three problems on the previous three days. The aim is to find
out what has really stuck, not to pass or fail.

- **Three problems, one of each kind:** predict the output of some code without running it,
  find and fix a bug, and write a function from scratch.
- **Closed book.** No lesson, no old files, no AI, nothing pasted. If you're stuck, move on
  and come back.
- **Self-checking.** The write-from-scratch and bug-fix problems come with automatic checks
  (unit tests in their simplest form, using `assert`). Day 25 upgrades these to `pytest`,
  and from then on you start writing some of the tests yourself.
- **Score yourself honestly.** Note which ones you missed. Anything missed gets revisited
  in the next lesson, and if a checkpoint goes badly, the next session is a redo of the
  shaky part. We add days rather than push on.

## Where you start

From your practice files, you could already:
- take input, use f-strings, if/elif/else, for loops
- write functions with parameters, work with lists and strings
- write simple classes and a tkinter window with try/except in it

## The 35 sessions

Legend: L = lesson, C = checkpoint, P = mini-project, R = catch-up and review.

| Day | Type | Topic | Notes |
| --- | --- | --- | --- |
| 1 | L | Functions that return a value | done |
| 2 | L | Input validation: try/except, while loops | in progress; p3 safe calculator still to do |
| 3 | L | Strings in depth: methods, slicing, formatting | fixes the uppercase vowel bug in `vowel_counter.py` |
| 4 | C | Checkpoint: Days 1-3 | |
| 5 | L | Lists in depth: methods, slicing, sorting with a key | |
| 6 | L | Tuples and sets: picking the right container | |
| 7 | L | Dictionaries | |
| 8 | C | Checkpoint: Days 5-7 | |
| 9 | P | Mini-project 1: command-line expense tracker | uses Days 1-7; stays in memory for now |
| 10 | L | Reading and writing text files | `with`, `pathlib` |
| 11 | L | CSV and JSON files | |
| 12 | C | Checkpoint: Days 9-11 | |
| 13 | L | Modules, imports, splitting code across files | `if __name__ == "__main__"` |
| 14 | L | Errors in depth: tracebacks, `raise`, your own messages | follows on from Day 2 |
| 15 | R | Catch-up and review | redo anything that didn't land |
| 16 | C | Checkpoint: Days 13-15 | |
| 17 | L | Comprehensions, `enumerate`, `zip`, `lambda` | |
| 18 | L | Dates and times | |
| 19 | P | Mini-project 2: log file analyzer | homelab flavour; uses files, dates, errors |
| 20 | C | Checkpoint: Days 17-19 | |
| 21 | L | Classes: `__init__`, methods, `__repr__` | builds on Dog and Car |
| 22 | L | Objects working together (composition) | builds on Human |
| 23 | L | Inheritance, and when not to use it | |
| 24 | C | Checkpoint: Days 21-23 | |
| 25 | L | Testing: `assert` and pytest | |
| 26 | L | Debugging: print, pdb, Zed's debugger | |
| 27 | P | Mini-project 3: asset tracker class that saves to JSON | adds tests of your own |
| 28 | C | Checkpoint: Days 25-27 | you write some of the tests yourself |
| 29 | L | Virtual environments and pip, properly | |
| 30 | L | HTTP and APIs with `requests` | |
| 31 | L | Command-line scripts with `argparse`; `subprocess` and `shutil` | dry-run first |
| 32 | C | Checkpoint: Days 29-31 | |
| 33 | P | Final project: choose it, plan it, start it | |
| 34 | P | Final project: finish it | |
| 35 | R | Review: read your own Pizza app with fresh eyes, plan what's next | |

## Bonus topics (not scheduled)

These didn't fit in 35 sessions. Say the word and I'll slot one in, or use it as a stretch:

- SQLite with `sqlite3`
- Regular expressions, the useful 20%
