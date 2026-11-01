# Day 7, Problem 2: Dictionaries and loops
#
# Write three functions. Each RETURNS a value; none prints or changes what it was given.
#
#   total_value(prices)       -> the sum of all the values in the dictionary.
#                                {"a": 2.5, "b": 1.5} -> 4.0        {} -> 0
#                                Hint: sum(prices.values())
#
#   most_common_word(text)    -> the word that appears most often, ignoring capitals.
#                                If two words tie, give the one that appeared first.
#                                "the cat the dog" -> "the"        "b a b a" -> "b"
#                                If there are no words, raise ValueError("No words.")
#                                Hint: build the counts like in Problem 1, then
#                                max(counts, key=counts.get)
#                                (max returns the first biggest one it meets, and a
#                                dictionary remembers the order things were added.)
#
#   group_by_length(words)    -> a dictionary: each length is a key, and its value is the
#                                list of words with that length, in their original order.
#                                ["a", "bb", "c", "dd"] -> {1: ["a", "c"], 2: ["bb", "dd"]}
#                                Hint: the "grouping" pattern from the lesson.
#
# Plan it as comments first, then one line at a time.


from multiprocessing import Value


def total_value(prices):
    # 1. return the sum of the values
    return sum(prices.values())



def most_common_word(text):
    # 1. split the lowercase text into words
    words = text.lower().split()
    # 2. no words? raise ValueError("No words.")
    if not words:
        raise ValueError("No words.")
    # 3. count the words in a dictionary
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    # 4. return the word with the biggest count
    return max(counts, key=counts.get)


def group_by_length(words):
    # 1. start with an empty dictionary called groups
    groups = {}
    # 2. for each word: find its length
    for word in words:

    #   if that length is not in groups yet, make an empty list for it
        length = len(word)
        if length not in groups:
            groups[length] = []

     #  append the word to groups[length]
        groups[length].append(word)

    # 3. return groups
    return groups


# ---- checks: don't edit this part ----
assert total_value({"a": 2.5, "b": 1.5}) == 4.0, "2.5 + 1.5 is 4.0"
assert total_value({}) == 0, "an empty dictionary totals 0"
assert total_value({"x": 10}) == 10, "one value totals itself"

assert most_common_word("the cat the dog") == "the", '"the" appears twice'
assert most_common_word("The THE the cat") == "the", "capitals are ignored"
assert most_common_word("b a b a") == "b", "a tie gives the one that appeared first"
assert most_common_word("solo") == "solo", "one word is the most common"
try:
    most_common_word("   ")
    assert False, "no words should raise ValueError"
except ValueError as e:
    assert str(e) == "No words.", 'the message should be "No words."'

assert group_by_length(["a", "bb", "c", "dd"]) == {1: ["a", "c"], 2: ["bb", "dd"]}, \
    "words should be grouped by length"
assert group_by_length([]) == {}, "[] should give {}"
assert group_by_length(["xyz"]) == {3: ["xyz"]}, "one word gives one group"
words = ["hi", "yo"]
group_by_length(words)
assert words == ["hi", "yo"], "the original list must not be changed"
print("All checks passed")
# ---- end of checks ----
