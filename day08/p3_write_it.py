# Day 8, Problem 3: Write it from scratch
#
# Closed book. Write both function bodies yourself; there is no hint code.
# Planning your steps as comments first is allowed, and a good idea.
#
#   total_by_item(pairs)  -> a dictionary of the total quantity for each item.
#                            "pairs" is a list of (item, quantity) tuples.
#
#       [("apple", 3), ("pear", 2), ("apple", 1)]  -> {"apple": 4, "pear": 2}
#       []                                         -> {}
#
#       If any quantity is below 0, raise ValueError with the message "Negative quantity."
#       Don't change the list that was passed in.
#
#   most_ordered(totals)  -> the item with the biggest total, from a dictionary like the
#                            one above.   {"apple": 4, "pear": 2} -> "apple"
#                            If two items tie, give the one that is listed first.
#                            If the dictionary is empty, raise ValueError with the message
#                            "Nothing to compare."
#
# Both functions must return their answers, not print them.


def total_by_item(pairs):
    # Start with empty dictionary
    totals = {}
    # Check each item and quantity
    for item, quantity in pairs:
        #Reject negative quantities
        if quantity < 0:
            raise ValueError("Negative quantity.")
        #Add quantity to the total items
        totals[item] = totals.get(item,0) + quantity
    # Return the totals
    return totals


def most_ordered(totals):
    # Reject an empty dictionary
    if not totals:
        raise ValueError("Nothing to compare.")
    # Return item with the largest total
    return max(totals, key=totals.get)


# ---- checks: don't edit this part ----
assert total_by_item([("apple", 3), ("pear", 2), ("apple", 1)]) == {"apple": 4, "pear": 2}, \
    "apple 3 + 1 = 4, pear 2"
assert total_by_item([]) == {}, "[] should give {}"
assert total_by_item([("a", 0)]) == {"a": 0}, "a quantity of 0 still counts as an entry"
assert total_by_item([("x", 1), ("x", 1), ("x", 1)]) == {"x": 3}, "one item added up three times"

orders = [("apple", 3), ("pear", 2)]
total_by_item(orders)
assert orders == [("apple", 3), ("pear", 2)], "the list that was passed in must not change"

try:
    total_by_item([("apple", 3), ("pear", -1)])
    assert False, "a negative quantity should raise ValueError"
except ValueError as e:
    assert str(e) == "Negative quantity.", 'the message should be "Negative quantity."'

assert most_ordered({"apple": 4, "pear": 2}) == "apple", "apple has the biggest total"
assert most_ordered({"a": 1, "b": 5, "c": 3}) == "b", "b has the biggest total"
assert most_ordered({"a": 2, "b": 2}) == "a", "a tie goes to the one listed first"
try:
    most_ordered({})
    assert False, "an empty dictionary should raise ValueError"
except ValueError as e:
    assert str(e) == "Nothing to compare.", 'the message should be "Nothing to compare."'
print("All checks passed")
# ---- end of checks ----
