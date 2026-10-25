# Extra practice 1: Working with a list of words
#
# This is OPEN BOOK. Use the lesson, the cheat sheet, and ask me anything.
# The idea: text.split() turns text into a LIST of words. Everything else is
# asking questions about that list.
#
#   words = "  hello   big world ".split()     ->  ["hello", "big", "world"]
#   len(words)   -> 3     how many words
#   words[0]     -> "hello"   the first word
#   words[-1]    -> "world"   the last word
#   words == []  (or len(words) == 0)   -> no words at all
#
# THE METHOD: do one step, print it, run it. Then the next step. Don't write all of
# it at once. Start with word_count since it is the shortest.
#
# Write three functions:
#
#   word_count(text)  -> how many words are in the text.
#                        "  hello   big world " -> 3     "" -> 0     "   " -> 0
#
#   first_word(text)  -> the first word, or "" if there are no words.
#                        "  hello big" -> "hello"        "" -> ""
#
#   last_word(text)   -> the last word. If there are no words, RAISE a ValueError
#                        with the message "No words."
#                        "  one " -> "one"
#
# Hint for last_word: it is the same as first_word, except the empty case raises
# an error instead of returning "". The raise line looks like this:
#
#       raise ValueError("No words.")


def word_count(text):
    words = text.split()     # 1. split the text into a list of words
    return len(words)        # 2. return how many words are in the list


def first_word(text):
    # 1. split the text into a list of words
    words = text.split()

    # 2. if there are no words, return ""
    if not words:
        return ""
    else:     # 3. otherwise return the first word
      return words[0]


def last_word(text):
    words  = text.split()      # 1. split the text into a list of words

    if not words:
            raise ValueError("No words.")      # 2. if there are no words, raise ValueError("No words.")
    else:
        return words[-1]


# ---- checks: don't edit this part ----
def raises_value_error(text):
    try:
        last_word(text)
    except ValueError:
        return True
    return False


assert word_count("hello") == 1, '"hello" is 1 word'
assert word_count("  hello   big world ") == 3, "extra spaces should not count as words"
assert word_count("") == 0, "empty text has 0 words"
assert word_count("   ") == 0, "only spaces has 0 words"

assert first_word("  hello big") == "hello", 'first word of "  hello big" is "hello"'
assert first_word("one") == "one", "a single word is its own first word"
assert first_word("") == "", 'empty text should give ""'
assert first_word("   ") == "", 'only spaces should give ""'

assert last_word("hello big world") == "world", 'last word is "world"'
assert last_word("  one ") == "one", "a single word is its own last word"
assert raises_value_error(""), "empty text should raise ValueError"
assert raises_value_error("   "), "only spaces should raise ValueError"
try:
    last_word("")
except ValueError as e:
    assert str(e) == "No words.", 'the message should be "No words."'
print("All checks passed")
# ---- end of checks ----
