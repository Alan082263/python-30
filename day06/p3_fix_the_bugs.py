# Day 6, Problem 3: Fix the bugs
#
# Each function below has ONE bug, and each bug is one of today's gotchas.
# First read the code and try to spot each bug without running anything.
# Then run the file: the checks will tell you which ones still fail.
#
# Rules: fix the functions only. Don't edit the checks at the bottom.
#
#   empty_set()               -> a new, empty SET
#   single_item_tuple(x)      -> a tuple that holds just x:  5 -> (5,)
#   with_item(items, x)       -> a NEW set: the items plus x.
#                                The set that was passed in must not change.


def empty_set():
    #return {}    # should be normal brackets
    return set()


def single_item_tuple(x):
    return (x,)    #needs a comma to designate a tuple


def with_item(items, x):
    # make a new copy of the original
    result = items.copy()

    #add an x
    result.add(x)

    # return the updated set
    return result



# ---- checks: don't edit this part ----
assert empty_set() == set(), "empty_set() should be an empty set"
assert isinstance(empty_set(), set), "empty_set() should be a set, not something else"

assert single_item_tuple(5) == (5,), "single_item_tuple(5) should be (5,)"
assert isinstance(single_item_tuple("a"), tuple), "single_item_tuple should give back a tuple"

original = {1, 2}
assert with_item(original, 3) == {1, 2, 3}, "with_item({1, 2}, 3) should be {1, 2, 3}"
assert original == {1, 2}, "with_item must not change the set that was passed in"
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write one comment line here for each bug, in your own words.
# empty_set:
# single_item_tuple:
# with_item:
