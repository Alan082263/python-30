# Day 5, Problem 3: Fix the bugs
#
# Each function below has ONE bug, and each bug is one of today's gotchas.
# First read the code and try to spot each bug without running anything.
# Then run the file: the checks will tell you which ones still fail.
#
# Rules: fix the functions only. Don't edit the checks at the bottom.
#
#   sorted_desc(numbers)       -> a list of the numbers, biggest first
#   with_item(items, x)        -> a NEW list: the items with x added on the end.
#                                 The list that was passed in must not change.
#   remove_negatives(numbers)  -> a list of only the numbers that are 0 or more


def sorted_desc(numbers):
    numbers = numbers.sort(reverse=True)
    return numbers


def with_item(items, x):
    result = items
    result.append(x)
    return result


def remove_negatives(numbers):
    for n in numbers:
        if n < 0:
            numbers.remove(n)
    return numbers


# ---- checks: don't edit this part ----
assert sorted_desc([3, 1, 2]) == [3, 2, 1], "sorted_desc([3, 1, 2]) should be [3, 2, 1]"
assert sorted_desc([]) == [], "sorted_desc([]) should be []"

original = [1, 2]
assert with_item(original, 3) == [1, 2, 3], "with_item([1, 2], 3) should be [1, 2, 3]"
assert original == [1, 2], "with_item must not change the list that was passed in"

assert remove_negatives([-1, -2, 3]) == [3], "remove_negatives([-1, -2, 3]) should be [3]"
assert remove_negatives([5, -1, 0, -7, 2]) == [5, 0, 2], "the order of the keepers is kept"
assert remove_negatives([]) == [], "remove_negatives([]) should be []"
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write one comment line here for each bug, in your own words.
