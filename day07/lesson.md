# Day 7: Dictionaries

About 30 minutes: 10 to read, 20 to solve, a few to commit.

## Warm-up: two traps from Day 6

Predict each output before reading the answers:

```python
x = {}
y = (5)
z = (5,)
print(type(x), type(y), type(z))        # A Missing closing bracket

colours = {"red", "blue"}
result = colours.add("pink")
print(result)                           # B None
```

Answers: **A** prints `<class 'dict'> <class 'int'> <class 'tuple'>`. `{}` is an empty
**dictionary**, which is today's topic. `(5)` is just a number, and `(5,)` is a tuple.
**B** prints `None`. Methods that change something in place return nothing.

## What a dictionary is

A dictionary stores **pairs**: a **key** and the **value** that goes with it. You look
things up by key, the way you look up a word in a real dictionary. Java's `HashMap` is the
match.

```python
prices = {"apple": 1.25, "banana": 0.5, "cherry": 4.0}

print(prices["apple"])          # 1.25                   look up by key
prices["date"] = 6.0            # add a new pair
prices["apple"] = 1.5           # change an existing one (same key = overwrite)
print(len(prices))              # 4                      how many pairs
print("banana" in prices)       # True                   `in` checks the KEYS
```

| Python | What it does | Java |
| --- | --- | --- |
| `d[key]` | the value, or **KeyError** if the key is missing | `get(key)` |
| `d[key] = value` | add or overwrite | `put(key, value)` |
| `d.get(key)` | the value, or `None` if missing | `get(key)` |
| `d.get(key, 0)` | the value, or 0 if missing | `getOrDefault(key, 0)` |
| `key in d` | is the key there? | `containsKey(key)` |
| `del d[key]` | remove a pair (KeyError if missing) | `remove(key)` |
| `d.pop(key)` | remove a pair AND give back its value | `remove(key)` |
| `d.pop(key, None)` | same, but no error if missing | |
| `len(d)` | number of pairs | `size()` |

The big one: **`d["zzz"]` crashes with `KeyError: 'zzz'` if the key isn't there**, while
`d.get("zzz")` quietly gives `None`. Use `get` when a missing key is normal. Use `d[key]` when
a missing key would be a real problem.

## Looping

```python
for name in prices:                       # keys
    print(name)

for price in prices.values():             # values
    print(price)

for name, price in prices.items():        # both: unpacking a tuple (Day 6)
    print(name, price)
```

Dictionaries **remember the order you added things in** (unlike sets), but you don't
look things up by position. There's no `d[0]`.

## Pattern 1: counting

This is the most useful dictionary move. "Add one to the count for this item, starting
from zero if we haven't seen it yet":

```python
counts = {}
for word in ["red", "blue", "red"]:
    counts[word] = counts.get(word, 0) + 1

print(counts)       # {'red': 2, 'blue': 1}
```

`counts.get(word, 0)` is the number so far, or 0 the first time. Write
`counts[word] += 1` instead and it crashes with `KeyError` on the very first word,
because there's no entry yet to add to. That's bug #1 of Problem 3.

## Pattern 2: grouping into lists

"Put each item in a bucket":

```python
groups = {}
for word in ["a", "bb", "c", "dd"]:
    size = len(word)
    if size not in groups:
        groups[size] = []           # make an empty bucket the first time
    groups[size].append(word)

print(groups)       # {1: ['a', 'c'], 2: ['bb', 'dd']}
```

## Finding the biggest, or sorting

```python
prices = {"apple": 1.25, "banana": 0.5, "cherry": 4.0}

print(max(prices, key=prices.get))        # cherry    the KEY with the biggest value
print(sorted(prices))                     # ['apple', 'banana', 'cherry']   keys, A to Z
print(sorted(prices, key=prices.get))     # ['banana', 'apple', 'cherry']   keys, cheapest first
print(sum(prices.values()))               # 5.75
```

Same `key=` idea as Day 5, and again it's `prices.get` with **no brackets**: you hand over the
function. `max` and `sorted` loop over the dictionary's *keys*, and `key=prices.get` says
"compare them by their values".

## Today's gotchas

- **`d[key]` on a missing key raises `KeyError`.** Use `d.get(key, default)` when that's
  expected.
- **Keys are unique.** Assigning to the same key twice overwrites the first value.
- **`in` looks at keys, not values.** `"apple" in prices` is True; `1.25 in prices` is False.
- **Keys must be unchangeable**: strings, numbers and tuples are fine, lists are not.
- **`d.update(...)` changes the dictionary and returns `None`.** Same family of trap as
  `sort()` and `add()`.
- **`b = a` doesn't copy.** Use `a.copy()`.
- **Don't add or remove entries while looping over a dictionary.** Python won't skip
  items like it does with lists. It stops with `RuntimeError: dictionary changed size during
  iteration`. Build a new dictionary of the entries you want to keep.

## Which container?

| You need... | Use |
| --- | --- |
| Items in order, repeats allowed | **list** |
| A small fixed bundle | **tuple** |
| Each item once, set maths | **set** |
| Look something up by name, or count things | **dictionary** |

## Your turn

Work inside the `day07` folder:

```bash
cd ~/Projects/python-30/day07
python3 p1_dict_basics.py
```

1. `p1_dict_basics.py`: three functions (count words, look up a price, swap keys and values).
2. `p2_dict_loops.py`: three functions (total the values, find the most common word, group words by length).
3. `p3_fix_the_bugs.py`: three functions, each with one of today's traps.

**Short on time?** Do p1 and stop. Same recipe: comments first, one line at a time, print
as you go.

## Finish: commit your work

On the **Mac**, in Terminal:

```bash
cd ~/Projects/python-30
git add .
git commit -m "Day 7: dictionaries"
git push
```

Day 8 is a checkpoint on Days 5 to 7: closed book, three problems, same format as Day 4.
