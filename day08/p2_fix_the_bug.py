# Day 8, Problem 2: Find and fix the bugs
#
# Closed book. This function has TWO bugs. Fix the function only; don't edit the checks.
#
#   top_words(text, n)  -> a list of the n most common words in the text, most common first.
#                          Ignore capitals. If two words are tied, the one that appeared
#                          first in the text comes first. If there are fewer than n
#                          different words, give back all of them.
#
#                          "the cat the dog the cat", 2  -> ["the", "cat"]
#
# Read the code first and try to spot the bugs by thinking, then run the checks.


def top_words(text, n):
    counts = {}
    for word in text.lower().split():
        # Fails first time and new word requires get.
        counts[word] = counts.get(word, 0) + 1
    # sorted needs counts.get without brackets
    ordered = sorted(counts, key=counts.get, reverse=True)
    return ordered[:n]


# ---- checks: don't edit this part ----
assert top_words("the cat the dog the cat", 2) == ["the", "cat"], "the, then cat"
assert top_words("b a b a c", 2) == ["b", "a"], "a tie goes to the word that appeared first"
assert top_words("The the THE cat", 1) == ["the"], "capitals are ignored"
assert top_words("one two", 5) == ["one", "two"], "fewer than n words: give them all"
assert top_words("", 3) == [], "no words should give []"
assert top_words("x y y", 1) == ["y"], "y appears twice, x once"
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write one comment line here for each bug, saying what it was.
# Fails first time and new word requires get
# sorted needs counts.get without brackets
#
