# Strings cheat sheet (Days 3 onward)

Keep this open while you work. It is not allowed at checkpoints, so use it to learn the
moves, not to avoid learning them.

## Picking characters and pieces

Say `word = "python"`.

| You want | Write | Result | Java |
| --- | --- | --- | --- |
| First character | `word[0]` | `"p"` | `charAt(0)` |
| Last character | `word[-1]` | `"n"` | `charAt(length() - 1)` |
| Length | `len(word)` | `6` | `length()` |
| First three | `word[:3]` | `"pyt"` | `substring(0, 3)` |
| From position 3 on | `word[3:]` | `"hon"` | `substring(3)` |
| Last three | `word[-3:]` | `"hon"` | `substring(length() - 3)` |
| Backwards | `word[::-1]` | `"nohtyp"` | no one-liner |

Slices stop BEFORE the second number. `word[2:5]` has 5 - 2 = 3 characters.
Single positions can crash (`word[6]` is an IndexError). Slices never crash.

## Changing and cleaning (each one returns a NEW string, so keep it)

| You want | Write | Example | Java |
| --- | --- | --- | --- |
| Lowercase | `s.lower()` | `"ABC"` -> `"abc"` | `toLowerCase()` |
| Uppercase | `s.upper()` | `"abc"` -> `"ABC"` | `toUpperCase()` |
| Capitalize each word | `s.title()` | `"alan wade"` -> `"Alan Wade"` | none |
| Trim the ends | `s.strip()` | `"  hi "` -> `"hi"` | `trim()` |
| Replace | `s.replace("a", "b")` | `"banana"` -> `"bbnbnb"` | `replace(...)` |
| Remove all spaces | `s.replace(" ", "")` | `"a b c"` -> `"abc"` | `replace(" ", "")` |

The classic mistake is `s.strip()` on a line by itself. The result is thrown away.
Write `s = s.strip()` or use the result directly.

## Breaking apart and gluing together

| You want | Write | Result |
| --- | --- | --- |
| Words, any spacing | `"  a   b ".split()` | `["a", "b"]` |
| Split on a character | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| Glue with single spaces | `" ".join(["a", "b"])` | `"a b"` |
| Glue with nothing | `"".join(["a", "b"])` | `"ab"` |

The string in front of `.join` is the GLUE. `" ".join(...)` glues with a space.

Standard tidy-up recipe: `" ".join(text.split())` (fixes all the spacing).

## Asking questions about a string (these give True/False or a number)

| You want | Write | Notes |
| --- | --- | --- |
| Is it inside? | `"@" in s` | True or False. Best for yes/no. |
| Starts with? | `s.startswith("ab")` | True or False |
| Ends with? | `s.endswith(".ca")` | True or False |
| Where is it? | `s.find("@")` | position, or -1 if missing |
| How many? | `s.count("a")` | a number |
| Same text? | `a == b` | compares the text (Java `equals`) |

Trap: `if s.find("@"):` is wrong. Position 0 counts as False and -1 counts as True.

## Looping and formatting

```python
for ch in "hello":          # ch is one character each time
    print(ch)

print(f"{4.5:.2f}")          # 4.50
print(f"{1234567:,}")        # 1,234,567
print(f"{'cat':>8}")         #      cat   (right-aligned in 8)
print(f"{7:03d}")            # 007
```

## When it goes wrong

| Message | Usually means |
| --- | --- |
| `IndexError: string index out of range` | you asked for a position that isn't there (`s[len(s)]`, or `s[0]` on `""`) |
| `TypeError: 'str' object does not support item assignment` | you tried `s[0] = "x"`. Build a new string instead. |
| a method "does nothing" | you didn't keep the result: `s = s.method()` |
| `AssertionError: ...` | a check failed. The message after the colon says which one. |

## Debug habit

When a function gives the wrong answer, call it with one simple input and print the
result. Then change one thing and run again.
