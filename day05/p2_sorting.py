# Day 5, Problem 2: Sorting
#
# Write three functions. Each RETURNS a new sorted list and leaves the original alone,
# so use sorted(...), not .sort().
#
#   sort_by_length(words)   -> the words, shortest first. Words of the same length keep
#                              their original order.
#                              ["pear", "fig", "banana", "kiwi"] -> ["fig", "pear", "kiwi", "banana"]
#                              Hint: sorted(..., key=len)
#
#   sort_names(names)       -> the names in alphabetical order, ignoring capitals.
#                              ["bob", "Alice", "carol"] -> ["Alice", "bob", "carol"]
#                              Hint: sorted(..., key=str.lower)  (the names themselves
#                              keep their original capitals)
#
#   top_three(numbers)      -> the three biggest numbers, biggest first. If there are
#                              fewer than three, give back all of them, biggest first.
#                              [5, 1, 9, 3, 7] -> [9, 7, 5]      [2, 8] -> [8, 2]
#                              Hint: sort biggest first with reverse=True, then take
#                              a slice of the first three.
#
# Remember: you write key=len, NOT key=len(). You hand over the function, you don't call it.


def sort_by_length(words):
    # 1. return the words sorted with the right key
    sorted_words = sorted(words, key=len)
    return sorted_words


def sort_names(names):
    # 1. return the names sorted with the right key
    sorted_names = sorted(names, key=str.lower)
    return sorted_names


def top_three(numbers):
    # 1. sort the numbers, biggest first
    sorted_numbers = sorted(numbers, reverse = True)
    # 2. return the first three of them
    return sorted_numbers[:3]


# ---- checks: don't edit this part ----
assert sort_by_length(["pear", "fig", "banana", "kiwi"]) == ["fig", "pear", "kiwi", "banana"], \
    "shortest first, ties keep their order"
assert sort_by_length([]) == [], "[] should give []"
original = ["ccc", "a", "bb"]
sort_by_length(original)
assert original == ["ccc", "a", "bb"], "the original list must not be changed"

assert sort_names(["bob", "Alice", "carol"]) == ["Alice", "bob", "carol"], \
    "capitals should be ignored when sorting"
assert sort_names(["Zoe", "adam", "Maya"]) == ["adam", "Maya", "Zoe"], \
    "the names keep their own capitals"
assert sort_names([]) == [], "[] should give []"

assert top_three([5, 1, 9, 3, 7]) == [9, 7, 5], "the three biggest, biggest first"
assert top_three([2, 8]) == [8, 2], "fewer than three: give them all, biggest first"
assert top_three([]) == [], "[] should give []"
numbers = [3, 1, 2]
top_three(numbers)
assert numbers == [3, 1, 2], "the original list must not be changed"
print("All checks passed")
# ---- end of checks ----
