# Day 7, Problem 3: Fix the bugs
#
# Each function below has ONE bug, and each bug is one of today's gotchas.
# First read the code and try to spot each bug without running anything.
# Then run the file: the checks will tell you which ones still fail.
#
# Rules: fix the functions only. Don't edit the checks at the bottom.
#
#   count_items(items)        -> a dictionary of how many times each item appears:
#                                ["a", "b", "a"] -> {"a": 2, "b": 1}
#   with_entry(d, key, value) -> a NEW dictionary: d plus the key/value pair.
#                                The dictionary that was passed in must not change.
#   remove_zeros(d)           -> a dictionary with only the entries whose value is not 0:
#                                {"a": 1, "b": 0, "c": 2} -> {"a": 1, "c": 2}


def count_items(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def with_entry(d, key, value):
    result =d.copy()
    result[key] = value
    return result


def remove_zeros(d):
    for key in list(d):
        if d[key] == 0:
            del d[key]
    return d


# ---- checks: don't edit this part ----
assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}, 'count_items(["a", "b", "a"]) should be {"a": 2, "b": 1}'
assert count_items([]) == {}, "count_items([]) should be {}"

original = {"x": 1}
assert with_entry(original, "y", 2) == {"x": 1, "y": 2}, "with_entry should add the pair"
assert original == {"x": 1}, "with_entry must not change the dictionary that was passed in"

assert remove_zeros({"a": 1, "b": 0, "c": 2}) == {"a": 1, "c": 2}, "the zero entry should be gone"
assert remove_zeros({"a": 0}) == {}, "remove_zeros({'a': 0}) should be {}"
assert remove_zeros({}) == {}, "remove_zeros({}) should be {}"
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write one comment line here for each bug, in your own words.
# count_items: Tried to increment a before adding to the dictionary causing an error
# with_entry: Return d.update(), changes the original dictionary and returns None

# remove_zeros:Deleted entrie from theoriginal dictionary while iterating over it
