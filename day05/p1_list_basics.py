# Day 5, Problem 1: List basics
#
# Write three functions. Each one RETURNS a new list or a number; none of them prints,
# and none of them changes the list it was given.
#
#   remove_first_and_last(items)  -> a new list without the first and last items.
#                                    [1, 2, 3, 4] -> [2, 3]      [1, 2] -> []
#                                    [1] -> []                   []     -> []
#                                    Hint: one slice does it, with a negative number.
#
#   average(numbers)              -> the average of the numbers, as a float.
#                                    [2, 4, 6] -> 4.0            [1, 2] -> 1.5
#                                    If the list is empty, raise ValueError("No numbers.")
#                                    Hint: sum(numbers) and len(numbers).
#
#   without_duplicates(items)     -> a new list with repeats removed, keeping the order
#                                    in which each item FIRST appeared.
#                                    [1, 2, 2, 3, 1] -> [1, 2, 3]
#                                    Hint: start with an empty list called result. For each
#                                    item, if it is not in result already, append it.
#
# THE METHOD: comments first (they are started for you), then one line at a time,
# printing as you go.


def remove_first_and_last(items):
    # 1. return a slice that skips the first item and the last item
    return items[1:-1]

def average(numbers):
    # 1. if there are no numbers, raise ValueError("No numbers.")
    if not numbers:
        raise ValueError("No numbers.")
# 2. otherwise return the total divided by how many there are
    return sum(numbers) / len(numbers)


def without_duplicates(items):
    # 1. start with an empty list called result
    result = []
    # 2. for each item in items:
    for item in items:
        #   if it is not in result yet, append it to result
        if item not in result:
            result.append(item)
    # 3. return result
    return result


# ---- checks: don't edit this part ----
def average_raises(numbers):
    try:
        average(numbers)
    except ValueError:
        return True
    return False


assert remove_first_and_last([1, 2, 3, 4]) == [2, 3], "[1, 2, 3, 4] should give [2, 3]"
assert remove_first_and_last([1, 2]) == [], "[1, 2] should give []"
assert remove_first_and_last([1]) == [], "[1] should give []"
assert remove_first_and_last([]) == [], "[] should give []"
data = [1, 2, 3]
remove_first_and_last(data)
assert data == [1, 2, 3], "the original list must not be changed"

assert average([2, 4, 6]) == 4.0, "average of [2, 4, 6] is 4.0"
assert average([1, 2]) == 1.5, "average of [1, 2] is 1.5"
assert average([5]) == 5.0, "average of [5] is 5.0"
assert average_raises([]), "an empty list should raise ValueError"
try:
    average([])
except ValueError as e:
    assert str(e) == "No numbers.", 'the message should be "No numbers."'

assert without_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3], "[1, 2, 2, 3, 1] should give [1, 2, 3]"
assert without_duplicates(["b", "a", "b"]) == ["b", "a"], "order of first appearance is kept"
assert without_duplicates([]) == [], "[] should give []"
print("All checks passed")
# ---- end of checks ----
