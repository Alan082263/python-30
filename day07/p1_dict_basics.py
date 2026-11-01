# Day 7, Problem 1: Dictionary basics
#
# Write three functions. Each one RETURNS a value; none of them prints, and none of them
# changes the dictionary it was given.
#
#   word_counts(text)         -> a dictionary of how many times each word appears.
#                                Ignore capitals. "The cat the DOG" -> {"the": 2, "cat": 1, "dog": 1}
#                                Empty text -> {}
#                                Hint: lowercase, split, then the counting pattern:
#                                counts[word] = counts.get(word, 0) + 1
#
#   price_of(menu, item)      -> the price of the item in the menu dictionary.
#                                If the item is not on the menu, raise ValueError("No such item.")
#                                Hint: check with  if item not in menu:
#
#   swap_keys_and_values(d)   -> a new dictionary where each value becomes a key and each
#                                key becomes its value.  {"a": 1, "b": 2} -> {1: "a", 2: "b"}
#                                Hint: start with an empty dictionary and loop with
#                                for key, value in d.items():
#
# THE METHOD: comments first (started for you), then one line at a time, printing as you go.


def word_counts(text):
    # 1. start with an empty dictionary called counts
    counts = {}
    # 2. for each word in the lowercase text, split into words:
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    # 3. return counts
    return(counts)



def price_of(menu, item):
    # 1. if the item is not in the menu, raise ValueError("No such item.")
    if item not in menu:
        raise ValueError("No such item.")

    # 2. otherwise return its price
    return menu[item]


def swap_keys_and_values(d):
    # 1. start with an empty dictionary called result
    result = {}

    # 2. for each key and value in d.items(): put result[value] = key
    for key, value in d.items():
        result[value] = key

    # 3. return result
    return result


# ---- checks: don't edit this part ----
assert word_counts("The cat the DOG") == {"the": 2, "cat": 1, "dog": 1}, "capitals are ignored"
assert word_counts("  a   a  a ") == {"a": 3}, "extra spaces are ignored"
assert word_counts("") == {}, 'empty text should give {}'

menu = {"apple": 1.25, "banana": 0.5}
assert price_of(menu, "apple") == 1.25, "apple costs 1.25"
assert price_of(menu, "banana") == 0.5, "banana costs 0.5"
try:
    price_of(menu, "cherry")
    assert False, "an item that is not on the menu should raise ValueError"
except ValueError as e:
    assert str(e) == "No such item.", 'the message should be "No such item."'
assert menu == {"apple": 1.25, "banana": 0.5}, "the menu must not be changed"

assert swap_keys_and_values({"a": 1, "b": 2}) == {1: "a", 2: "b"}, "keys and values should swap"
assert swap_keys_and_values({}) == {}, "{} should give {}"
original = {"x": 10}
swap_keys_and_values(original)
assert original == {"x": 10}, "the original dictionary must not be changed"
print("All checks passed")
# ---- end of checks ----
