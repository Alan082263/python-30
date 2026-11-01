# Day 6, Problem 1: Tuples
#
# Write three functions. Each one RETURNS a tuple. None of them prints.
#
#   min_and_max(numbers)  -> a tuple of (smallest, biggest).
#                            [4, 9, 2] -> (2, 9)       [5] -> (5, 5)
#                            If the list is empty, raise ValueError("No numbers.")
#                            Hint: min(...) and max(...), then return both with a comma.
#
#   swap_pair(pair)       -> a new tuple with the two items swapped.
#                            (1, 2) -> (2, 1)          ("a", "b") -> ("b", "a")
#                            Hint: unpack the pair into two names first.
#
#   split_name(full_name) -> a tuple of (first, last), each with a capital first letter.
#                            "alan george WADE" -> ("Alan", "Wade")
#                            One word: the last part is an empty string. "cher" -> ("Cher", "")
#                            If the name is empty or only spaces, raise ValueError("Name is empty.")
#                            Hint: this is Day 4's format_name again, but you return a tuple.
#
# THE METHOD: comments first (started for you), then one line at a time, printing as you go.


def min_and_max(numbers):
    # 1. if there are no numbers, raise ValueError("No numbers.")
    if not numbers:
        raise ValueError("No numbers.")
    # 2. otherwise return the smallest and the biggest, separated by a comma
    return min(numbers), max(numbers)


def swap_pair(pair):
    # 1. unpack the pair into two names, like  first, second = pair
    first, second = pair
    # 2. return them the other way round
    return second, first
print(swap_pair((1, 2)))  #2,1


def split_name(full_name):
    # 1. split the name into words
    words = full_name.split()

    # 2. no words? raise ValueError("Name is empty.")
    if not words:
        raise ValueError("Name is empty.")

    # 3. one word? return that word capitalized, and an empty string
    if len(words) == 1:
        return words[0].capitalize(), ""

    # 4. otherwise return the first word and the last word, each capitalized
    return words[0].capitalize(), words[-1].capitalize()


# ---- checks: don't edit this part ----
def raises_value_error(function, argument):
    try:
        function(argument)
    except ValueError:
        return True
    return False


assert min_and_max([4, 9, 2]) == (2, 9), "min_and_max([4, 9, 2]) should be (2, 9)"
assert min_and_max([5]) == (5, 5), "min_and_max([5]) should be (5, 5)"
assert raises_value_error(min_and_max, []), "an empty list should raise ValueError"
try:
    min_and_max([])
except ValueError as e:
    assert str(e) == "No numbers.", 'the message should be "No numbers."'
low, high = min_and_max([7, 3, 8])
assert (low, high) == (3, 8), "you should be able to unpack the result into two names"

assert swap_pair((1, 2)) == (2, 1), "swap_pair((1, 2)) should be (2, 1)"
assert swap_pair(("a", "b")) == ("b", "a"), 'swap_pair(("a", "b")) should be ("b", "a")'
assert isinstance(swap_pair((1, 2)), tuple), "swap_pair should give back a tuple"

assert split_name("alan george WADE") == ("Alan", "Wade"), "first and last, capitalized"
assert split_name("  alan   wade  ") == ("Alan", "Wade"), "extra spaces ignored"
assert split_name("cher") == ("Cher", ""), 'one word should give ("Cher", "")'
assert raises_value_error(split_name, ""), "empty text should raise ValueError"
assert raises_value_error(split_name, "   "), "only spaces should raise ValueError"
try:
    split_name("")
except ValueError as e:
    assert str(e) == "Name is empty.", 'the message should be "Name is empty."'
print("All checks passed")
# ---- end of checks ----
