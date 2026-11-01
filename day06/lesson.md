# Day 6: Tuples and sets: picking the right container

About 30 minutes: 8 to read, 20 to solve, a few to commit.

## Warm-up: two traps from Day 5

Predict each output before reading the answers:

```python
a = [3, 1, 2]
b = a
b.append(9)
print(a)                    # A

nums = [3, 1, 2]
result = nums.sort()
print(result)               # B
```

Answers: **A** prints `[3, 1, 2, 9]` (`b = a` is another name for the same list, not a copy).
**B** prints `None` (`sort()` changes the list in place and returns nothing).

Keep both in mind. Today's sets have the same `None` rule.

## Tuples: a fixed bundle

A tuple looks like a list with round brackets, but **it can't be changed** after it's made,
like a string:

```python
point = (3, 4)

print(point[0])         # 3
print(point[-1])        # 4
print(len(point))       # 2
point[0] = 9            # TypeError: 'tuple' object does not support item assignment
```

Java has no direct match (the nearest are a small record class, or an immutable list).
Python uses tuples all the time, mostly for two jobs.

**Job 1: handing back more than one value.** A function can return several things at once.
It's really one tuple:

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

print(min_and_max([4, 9, 2]))       # (2, 9)

low, high = min_and_max([4, 9, 2])  # "unpacking": one name for each piece
print(low, high)                    # 2 9
```

**Job 2: a small record whose parts belong together and never change:** a point `(3, 4)`,
a date `(2026, 10, 26)`, a name `("Alan", "Wade")`.

Unpacking also gives you the classic swap, with no temporary variable:

```python
a = 1
b = 2
a, b = b, a
print(a, b)             # 2 1
```

**The one-item trap:** `(5)` is just the number 5 in brackets. A tuple with one item needs a
trailing comma:

```python
print((5))              # 5       a number
print((5,))             # (5,)    a tuple
```

Tuples only have two methods, `count` and `index`, since nothing can be added or removed.

## Sets: unique items, fast "is it in there?"

A set holds each item **at most once**, in no particular order. Java's `HashSet` is the match.

```python
colours = {"red", "green", "red", "blue"}
print(len(colours))             # 3        the second "red" was ignored
print("red" in colours)         # True

colours.add("pink")             # add an item
colours.discard("green")        # remove it; fine if it isn't there
colours.remove("zzz")           # KeyError: remove complains if it isn't there
```

Three things to remember:

1. **An empty set is `set()`, NOT `{}`.** `{}` is an empty *dictionary* (Day 7).
2. **No order, no positions.** `colours[0]` is an error. When you print a set the items can
   come out in any order, so if you need a stable order, use `sorted(colours)`, which
   gives a list.
3. **`add` returns `None`**, just like `append` and `sort` on lists. It changes the set in
   place. Never write `s = s.add(x)`.

### Set maths

The real power of sets is the maths:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)     # {1, 2, 3, 4, 5}   union: everything in either
print(a & b)     # {3, 4}            intersection: in both
print(a - b)     # {1, 2}            in a but not in b
print(a ^ b)     # {1, 2, 5}         in one or the other, but not both
```

### Removing duplicates the quick way

```python
numbers = [1, 2, 2, 3, 1]
print(sorted(set(numbers)))         # [1, 2, 3]
```

`set(numbers)` drops the repeats, and `sorted(...)` turns it back into a list in a steady
order. Compare it with your `without_duplicates` from Day 5: the set version is one line,
but it **loses the original order**. Yours kept it. Choosing between them is the lesson.

### What can go in a set

Items must be unchangeable, so a **tuple** can go in a set, but a **list** can't:

```python
{(1, 2), (3, 4)}        # fine
{[1, 2]}                # TypeError: unhashable type: 'list'
```

## Which container should I use?

| You need... | Use |
| --- | --- |
| Items in order, repeats allowed, add and remove as you go | **list** |
| A small fixed bundle that shouldn't change, or to return several values | **tuple** |
| Each item only once, quick "is it in there?", or "what do these two have in common?" | **set** |

Quick tests: *Does order matter?* then list or tuple. *Do repeats matter?* If you want them
gone, set. *Will it change after I make it?* If not, tuple.

## Today's gotchas

- `(5)` is not a tuple. `(5,)` is.
- `{}` is an empty dictionary. `set()` is the empty set.
- A set has no order and no `[0]`. Use `sorted(...)` when you need a steady list.
- `add` returns `None`. Don't assign it.
- A tuple can't be changed, but you can build a new one: `(new,) + old[1:]`.

## Your turn

Work inside the `day06` folder:

```bash
cd ~/Projects/python-30/day06
python3 p1_tuples.py
```

1. `p1_tuples.py`: three functions that return tuples (min and max, swapping a pair, splitting a name).
2. `p2_sets.py`: three functions using set maths.
3. `p3_fix_the_bugs.py`: three functions, each with one of today's traps.

**Short on time?** Do p1 and stop. Remember the recipe: comments first, one line at a
time, print as you go.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .
git commit -m "Day 6: tuples and sets"
git push
```

Day 7 is dictionaries, the last container, and probably the most useful one.
