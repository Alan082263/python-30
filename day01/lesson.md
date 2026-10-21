# Day 1: Functions that return a value

About 30 minutes: 5 to read, 20 to solve, a few to commit.

## The idea

A function should work out an answer and hand it back with `return`. Whoever called the
function decides what to do with the answer: print it, add it to something, store it.

Your `momentum_out` function in `practice/problems/math/object_speed_mass.py` does the
maths and the printing in one place:

```python
def momentum_out(mass, speed):
    momentum = (mass * speed)
    print("The momentum of the object is:", momentum, "kg·m/s")
```

That works, but the answer is trapped inside the print. You can't add two momenta
together, compare them, or save one to a file. Here is the same function, split into
the two jobs:

```python
def momentum(mass, speed):
    return mass * speed          # job 1: work out the answer


p = momentum(2.0, 3.0)           # the answer comes back here
print(f"Momentum: {p} kg·m/s")   # job 2: show it, outside the function

total = momentum(1.5, 4) + momentum(2, 2)   # reuse: only possible because it returns
print(total)
```

## Why it matters

- **Reuse.** A returned value can go into other calculations. A printed one can't.
- **Testing.** You can check a returned value automatically. That is how the checks at the
  bottom of today's problem files work.
- **Clarity.** One function, one job.

If you think in Java, this is the difference between a method that returns `double` and
one that is `void` and calls `System.out.println`.

## What a function returns when you forget `return`

Python quietly gives back `None`. Try this in a scratch file:

```python
def add(a, b):
    total = a + b       # no return

answer = add(2, 3)
print(answer)           # prints None
```

Most of today's bugs will be this one, or its cousin: `return` placed inside a loop, where
it ends the whole function on the first pass.

## Setup, one time (about 5 minutes)

Run these on the **Mac**, in Terminal (or in Zed's terminal panel):

```bash
python3 --version                      # just reports the version; changes nothing
cd ~/Projects/python-30
git init                               # makes this folder a git repo (adds a hidden .git folder)
```

Open the folder in Zed: File > Open, choose `python-30`. Open the terminal panel from the
View menu, or with Ctrl+` (backtick).

We skip virtual environments until Day 22. Everything until then uses only what ships
with Python, so there is nothing to install and nothing to isolate.

If you're signed in to Zed it may show AI "edit predictions" as you type. For practice
you'll probably want those off: open Settings (Cmd+,) and search for "edit prediction".

## Your turn

Work inside the `day01` folder. Run a problem from the terminal like this:

```bash
cd ~/Projects/python-30/day01
python3 p1_temperature.py
```

If a check fails you'll see an `AssertionError` with a message saying which one. That is
the file telling you what to fix, not a crash to worry about.

1. `p1_temperature.py`: two converter functions, then a small interactive program.
2. `p2_receipt_helpers.py`: three functions, one of which calls another.
3. `p3_fix_the_bugs.py`: three broken functions. Read each one, find the bug, fix it with
   the smallest change you can.

**Stretch (if you have time):** copy `practice/problems/math/object_speed_mass.py` into
`day01` (copy it, don't edit the original) and rewrite it so `momentum_out` becomes a
function that returns the momentum, with the `print` outside it.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .                              # stages everything new or changed in this folder
git commit -m "Day 1: functions that return"
```

If you push this to GitHub, keep the repository private.
