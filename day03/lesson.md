# Day 3: Strings in depth

About 30 minutes: 8 to read, 20 to solve, a few to commit.

## Why this day exists

Your `vowel_counter.py` counts `a e i o u` but misses capitals, so `"HELLO"` gives the wrong
answer. That's a string bug, and by the end of today you'll know exactly why it happens and
how to fix it in one line.

## A string is a row of characters

You can pick characters out by position. Counting starts at 0, same as Java:

```python
word = "python"

print(word[0])      # p        (Java: word.charAt(0))
print(word[2])      # t
print(word[-1])     # n        negative counts from the END
print(word[-2])     # o
print(len(word))    # 6        (Java: word.length())
```

`word[-1]` is the big new idea. Java has no equivalent; you'd write
`word.charAt(word.length() - 1)`. In Python the last character is just `[-1]`.

Going past the end is an error: `word[6]` raises `IndexError: string index out of range`,
because the valid positions are 0 to 5.

## Slicing: take a piece

`text[start:stop]` gives the characters from `start` up to, but **not including**, `stop`:

```python
word = "python"

print(word[0:2])    # py       (Java: word.substring(0, 2))
print(word[2:5])    # tho
print(word[:3])     # pyt      leave out start: from the beginning
print(word[3:])     # hon      leave out stop: to the end
print(word[-3:])    # hon      the last three characters
print(word[::-1])   # nohtyp   the whole thing, backwards
```

Two tricks to remember:
- The length of `text[a:b]` is `b - a`. `word[2:5]` is 3 characters.
- Slicing never crashes for going too far. `word[3:100]` just gives `"hon"`. Only
  *single* positions like `word[100]` raise `IndexError`.

## Strings are immutable (and this causes the #1 beginner bug)

Same as Java: a string can't be changed in place.

```python
word = "python"
word[0] = "P"       # TypeError: 'str' object does not support item assignment
```

Every string method **returns a new string** and leaves the original alone:

```python
name = "  alan  "
name.strip()        # returns "alan"... and throws it away!
print(name)         # still "  alan  "

name = name.strip() # keep the result by assigning it
print(name)         # alan
```

If a string method seems to do nothing, check that you actually kept the result.

## Methods you'll use constantly

| Python | What it does | Java |
| --- | --- | --- |
| `s.upper()` / `s.lower()` | change case | `toUpperCase()` / `toLowerCase()` |
| `s.strip()` | remove spaces at both ends | `trim()` |
| `s.replace("a", "b")` | replace every match | `replace(...)` |
| `s.startswith("ab")` / `s.endswith("ab")` | true or false | `startsWith` / `endsWith` |
| `s.split()` | break into a list of words | `split(" +")` (but cleaner) |
| `", ".join(pieces)` | glue a list into one string | `String.join(", ", pieces)` |
| `s.count("a")` | how many times | no direct version |
| `"a" in s` | is it somewhere inside? | `contains("a")` |
| `s.find("a")` | position of first match, or **-1** | `indexOf("a")` |
| `s.title()` | Capitalize Each Word | no direct version |

Two of these deserve a closer look.

**`find` vs `in`.** `find` returns the *position*, and `-1` if there's no match. That
trips people up:

```python
text = "hello"
if text.find("h"):      # find returns 0, and 0 counts as False. Bug!
    print("found")
```

When you only want yes/no, use `in`: `if "h" in text:`. When you want the position, use
`find` and compare to `-1` explicitly: `if text.find("h") != -1:`.

**`split()` with no argument** splits on any run of whitespace and ignores the extra
spaces. `"  alan   wade ".split()` gives `["alan", "wade"]`. Then `" ".join(...)` puts them
back with exactly one space between. That's the standard tidy-up recipe.

## `==` compares the text

In Java, `==` on strings compares *identity* and you must use `.equals()`. In Python,
`==` compares the actual text, so it's what you want. (`is` is for `None`, as in Day 2.)

```python
print("abc" == "ab" + "c")    # True
```

## Looping over a string

```python
for ch in "hello":
    print(ch)
```

Each pass, `ch` is one character. No need for `charAt` or an index counter.

## Formatting numbers in f-strings

You already use f-strings. Add a colon and a format after the value:

```python
price = 4.5
print(f"${price:.2f}")        # $4.50      two decimals
print(f"{1234567:,}")         # 1,234,567  thousands separators
print(f"{'cat':>8}|")         #      cat|  right-aligned in 8 spaces
print(f"{'cat':<8}|")         # cat     |  left-aligned
print(f"{7:03d}")             # 007        padded with zeros to 3 digits
```

## The vowel counter fix

Your bug: `"A"` is not equal to `"a"`, so capitals were skipped. The fix is to compare
against a lowercase copy. If `text` is the user's string:

```python
lowered = text.lower()
```

and then count the vowels in `lowered` instead of `text`. Do that in Problem 2.

## Today's gotchas

- A string method returns a new string. If you don't assign it, it's gone.
- `find` returns `-1`, not `None` or `False`, when nothing matches. `-1` counts as true.
- `text[len(text)]` is always off the end. The last position is `len(text) - 1`, or just `-1`.
- Slices stop *before* the second number.

## Your turn

Work inside the `day03` folder. Run a problem from the terminal like this:

```bash
cd ~/Projects/python-30/day03
python3 p1_string_toolkit.py
```

1. `p1_string_toolkit.py`: three small string functions (first and last, palindrome, name tidy-up).
2. `p2_vowels_and_email.py`: your fixed vowel counter, plus hiding most of an email address.
3. `p3_fix_the_bugs.py`: three functions, each with a bug from today's gotchas. Find them
   by *reading* first, then run the checks.

**Stretch (if you have time):** copy `Projects/Basic/vowel_counter.py` (or wherever yours
lives) into `day03`, and fix it with `lower()`. Copy, don't edit the original.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .
git commit -m "Day 3: strings"
git push
```

Day 4 is the first checkpoint: three closed-book problems on Days 1 to 3.
