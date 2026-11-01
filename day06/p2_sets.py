# Day 6, Problem 2: Sets
#
# Write three functions. The first returns a number; the other two return a SORTED LIST
# (sets have no order, so sorted(...) gives a steady, testable answer).
#
#   unique_count(items)     -> how many different items there are.
#                              [1, 2, 2, 3, 1] -> 3        [] -> 0
#                              Hint: turn the list into a set, then len(...).
#
#   common_items(a, b)      -> a sorted list of the items that appear in BOTH lists,
#                              each one once.
#                              [1, 2, 2, 3], [2, 3, 4] -> [2, 3]
#                              Hint: turn both into sets and use &, then sorted(...).
#
#   only_in_first(a, b)     -> a sorted list of the items that are in a but NOT in b.
#                              [1, 2, 3], [2] -> [1, 3]
#                              Hint: sets and the - operator, then sorted(...).
#
# Remember: the original lists must not change. Making a set from a list does not change it.


def unique_count(items):
    # 1. make a set from the items
    set_items = set(items)
    # 2. return how many are in it
    return len(set_items)


def common_items(a, b):
    # 1. make a set from a, and a set from b
    set_a = set(a)
    set_b = set(b)

    # 2. find what is in both of them
    return sorted(set_a & set_b)


def only_in_first(a, b):
    # 1. make a set from a, and a set from b
    set_a = set(a)
    set_b = set(b)

    # 2. find what is in the first but not the second
    difference = set_a - set_b

    # 3. return it as a sorted list
    return sorted(difference)


# ---- checks: don't edit this part ----
assert unique_count([1, 2, 2, 3, 1]) == 3, "[1, 2, 2, 3, 1] has 3 different items"
assert unique_count([]) == 0, "[] has 0 different items"
assert unique_count(["a", "A", "a"]) == 2, '"a" and "A" are different items'

assert common_items([1, 2, 2, 3], [2, 3, 4]) == [2, 3], "[2, 3] are in both"
assert common_items([1, 2], [3, 4]) == [], "nothing in common should give []"
assert common_items([], [1]) == [], "an empty list has nothing in common"
assert isinstance(common_items([1], [1]), list), "common_items should give back a list"

assert only_in_first([1, 2, 3], [2]) == [1, 3], "1 and 3 are only in the first"
assert only_in_first([5, 5, 6], [6]) == [5], "repeats are removed, so just [5]"
assert only_in_first([1], [1]) == [], "everything is in both, so []"
first = [3, 1, 2]
second = [2]
only_in_first(first, second)
assert first == [3, 1, 2] and second == [2], "the original lists must not be changed"
print("All checks passed")
# ---- end of checks ----
