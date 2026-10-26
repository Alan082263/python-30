# Day 5: Lists in depth

About 30 minutes: 8 to read, 20 to solve, a few to commit.

## Warm-up: the trap from Day 4, one more time

Predict each output before reading the answers. Strings first, then lists:

```python
s = "hello"
s.upper()
print(s)                    # A

nums = [3, 1, 2]
nums.sort()
print(nums)                 # B

nums = [3, 1, 2]
nums = nums.sort()
print(nums)                 # C
```

Answers: **A** prints `hello` (strings are immutable, so the result was thrown away).
**B** prints `[1, 2, 3]`. **C** prints `None`.

Why do B and C differ from the string? **Lists can be changed in place; strings can't.**
`nums.sort()` rearranges the list itself and returns `None` to tell you "nothing new to give
you, I changed it". So `nums = nums.sort()` overwrites your list with `None`. That's the
list version of the trap, and it's bug #1 of Problem 3.

Rule of thumb:
- **String methods** make a new string. Keep the result.
- **List methods that change a list** (`sort`, `append`, `remove`, ...) change it in place
  and return `None`. Don't assign the result.

## The basics (same moves as strings)

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])        # apple         first        (Java: fruits.get(0))
print(fruits[-1])       # date          last
print(fruits[1:3])      # ['banana', 'cherry']   slice, stops BEFORE 3
print(fruits[:2])       # ['apple', 'banana']
print(fruits[::-1])     # reversed copy
print(len(fruits))      # 4             (Java: fruits.size())
print("fig" in fruits)  # False         is it in the list?

for fruit in fruits:    # one item at a time
    print(fruit)
```

A slice of a list is a **new list**, same as a slice of a string is a new string.

## Methods that change the list in place

| Python | What it does | Java |
| --- | --- | --- |
| `items.append(x)` | add x to the end | `add(x)` |
| `items.insert(0, x)` | add x at position 0 | `add(0, x)` |
| `items.extend(other)` | add every item of another list | `addAll(other)` |
| `items.remove(x)` | remove the first x. ValueError if missing! | `remove(Object)` |
| `items.pop()` | remove AND return the last item | `remove(size() - 1)` |
| `items.pop(0)` | remove AND return the item at position 0 | `remove(0)` |
| `items.sort()` | sort in place, returns `None` | `Collections.sort(items)` |
| `items.reverse()` | reverse in place, returns `None` | `Collections.reverse(items)` |

Every one of those changes the list itself. `pop` is the odd one: it changes the list *and*
gives you something back.

## Functions that give you something back (the original is untouched)

| Python | Gives back |
| --- | --- |
| `sorted(items)` | a NEW sorted list. The original stays as it was. |
| `len(items)`, `sum(numbers)`, `min(numbers)`, `max(numbers)` | a number |
| `items.count(x)` | how many times x appears |
| `items.index(x)` | the position of the first x (ValueError if missing) |
| `items.copy()` or `items[:]` | a NEW list with the same items |

Use `sorted(...)` when you want a sorted version and don't want to disturb the original.
Use `.sort()` when you want to sort the list you have.

## Sorting with a key

By default `sorted` puts numbers smallest to biggest, and text in alphabetical order (with
capitals before lowercase). To sort by something else, give it a **key**: a function that
takes one item and returns what to compare.

```python
words = ["pear", "fig", "banana", "kiwi"]

print(sorted(words, key=len))             # ['fig', 'pear', 'kiwi', 'banana']  by length
print(sorted(words, reverse=True))        # Z to A
print(sorted(["bob", "Alice", "carol"], key=str.lower))   # ['Alice', 'bob', 'carol']
```

- `key=len` means "compare by the length of each word".
- `key=str.lower` means "compare as if everything were lowercase" (the original text is
  not changed).
- Notice `pear` came before `kiwi`, both being 4 letters long. Sorting is **stable**: items
  that tie keep their original order.
- You write `key=len`, NOT `key=len(...)`. You're handing over the function itself, not
  calling it.

You can also give your own function as the key:

```python
def last_letter(word):
    return word[-1]

print(sorted(["pear", "fig", "banana"], key=last_letter))   # ['banana', 'pear', 'fig']
```

(Day 17 shows a shortcut for this called `lambda`. For now, a normal `def` is fine.)

## Two gotchas that bite everyone

**1. `b = a` does NOT make a copy.** Java is the same, and it surprises people there too.

```python
a = [1, 2, 3]
b = a               # b is another NAME for the same list
b.append(4)
print(a)            # [1, 2, 3, 4]   a changed too!

c = a.copy()        # a real copy
c.append(5)
print(a)            # still [1, 2, 3, 4]
```

**2. Don't remove items from a list while looping over it.** Python moves along by position,
so removing an item shifts the rest and the loop skips one.

```python
nums = [-1, -2, 3]
for n in nums:
    if n < 0:
        nums.remove(n)
print(nums)         # [-2, 3]   the -2 was skipped!
```

The fix is to build a NEW list of the items you want to keep:

```python
keepers = []
for n in nums:
    if n >= 0:
        keepers.append(n)
```

## The recipe still applies

Write your steps as comments first. Then one comment, one line, print, run. The files have
the comments started for you.

## Your turn

Work inside the `day05` folder:

```bash
cd ~/Projects/python-30/day05
python3 p1_list_basics.py
```

1. `p1_list_basics.py`: three functions that build and return new lists (slicing, an average
   with a `raise`, removing duplicates).
2. `p2_sorting.py`: three functions using `sorted` with a key.
3. `p3_fix_the_bugs.py`: three functions, each with one of today's list traps.

**Short on time?** Do p1 and stop. Same as before.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .
git commit -m "Day 5: lists"
git push
```

Day 6 is tuples and sets, which fit straight on from today.
