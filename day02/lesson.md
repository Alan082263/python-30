# Day 2: Input validation with try/except and while loops

About 30 minutes: 5 to read, 20 to solve, a few to commit.

## The problem

Your `calc.py` does this:

```python
first_number = float(input("Enter the first number: "))
```

Type `abc` and the program dies with a traceback:

```
ValueError: could not convert string to float: 'abc'
```

Its own spec says "Validates that the inputs are numbers", so this is a bug, and today you fix it.

## Reading a traceback

Read it from the bottom up. The last line says *what* went wrong (`ValueError`, with a
message). The lines above it say *where* (file, line number, the line itself). Most of the
time the last line plus the line number is all you need.

## try / except

`try` means "attempt this". `except` means "if it fails in this particular way, do this
instead of crashing":

```python
text = input("Enter a number: ")

try:
    number = float(text)
except ValueError:
    print("That wasn't a number.")
```

If `float(text)` works, the `except` block is skipped. If it raises `ValueError`, Python
jumps straight to the `except` block and the program carries on.

**Always name the error you expect** (`except ValueError`). Never write a bare `except:`.
A bare one also swallows typos in your own code and even Ctrl+C, so real bugs vanish and
you spend an hour wondering why nothing happens. Java comparison: this is
`catch (NumberFormatException e)` rather than `catch (Exception e)`.

## Turning failure into a return value

Yesterday's lesson says functions should return answers. Here is a function that returns
a number if it can, and `None` if it can't:

```python
def parse_number(text):
    try:
        return float(text)
    except ValueError:
        return None


print(parse_number("4.5"))    # 4.5
print(parse_number("abc"))    # None
```

The caller checks `if value is None:`. Use `is None`, not `== None`. (`None` is a single
object, and `is` asks "is it that exact object?".)

## while loops: keep asking until it's right

```python
while True:
    value = parse_number(input("Enter a number: "))
    if value is not None:
        break                    # leaves the loop
    print("Please enter a number, like 3 or 4.5.")

print(f"You entered {value}")
```

`while True` loops forever until something runs `break`. If you ever write one that
doesn't stop, press **Ctrl+C** in the terminal. That interrupts the program and is
harmless.

Another way to leave a loop is `return`. If the loop is inside a function, `return` exits
the whole function immediately. That is the Day 1 bug in reverse: today you *want* it.

You can also count attempts and give up:

```python
attempts = 0
while attempts < 3:
    attempts += 1
    ...
```

## Today's gotchas

- `input()` always gives you a `str`, even if the user types `5`. Converting is your job.
- `int("2.5")` raises `ValueError`, but `int(2.5)` quietly gives `2`. Strings and numbers
  behave differently.
- `float("nan")` and `float("inf")` are accepted by Python as valid floats. That's real
  behaviour, not a bug, but it surprises people. See the stretch in Problem 1.

## Your turn

Work inside the `day02` folder. Run a problem from the terminal like this:

```bash
cd ~/Projects/python-30/day02
python3 p1_parse_number.py
```

1. `p1_parse_number.py`: `parse_number` function, then a loop that keeps asking.
2. `p2_whole_number_in_range.py`: same idea for whole numbers within limits, with a
   3-attempt limit.
3. `p3_safe_calculator.py`: your calculator, rebuilt so nothing the user types can crash
   it. This one introduces `raise`.

**Stretch (if you have time):** copy `Projects/Basic/Calculator/calc.py` into `day02`
(copy, don't edit the original) and fix its input lines using `parse_number` in a loop.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .
git commit -m "Day 2: input validation"
```
