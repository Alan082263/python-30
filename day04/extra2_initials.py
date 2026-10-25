# Extra practice 2: Doing something with every word
#
# OPEN BOOK. Same idea as extra 1, plus one new move: a for loop over the list of words.
#
#   for word in ["alan", "wade"]:
#       print(word)            # prints alan, then wade
#
# And one more: building a string up piece by piece. Strings can't be changed, but you
# can make a new, longer one and keep it under the same name:
#
#       result = ""
#       result = result + "A"      # result is now "A"
#       result = result + "W"      # result is now "AW"
#
# Write the function:
#
#   initials(full_name)  -> the first letter of every word, in capitals, joined together.
#                           "Alan George Wade" -> "AGW"
#                           "alan wade"        -> "AW"
#                           "  june  "         -> "J"
#                           ""  -> ""          "   " -> ""
#
# THE METHOD: write the steps as comments first, then one step at a time,
# printing as you go. The steps are already below.


def initials(full_name):
    # 1. split the name into a list of words
    # 2. start with an empty string called result
    # 3. for each word in the list:
    #        add the word's first letter, in capitals, to result
    # 4. return result
    pass  # replace this line


# ---- checks: don't edit this part ----
assert initials("Alan George Wade") == "AGW", '"Alan George Wade" should give "AGW"'
assert initials("alan wade") == "AW", 'lowercase names should still give capitals: "AW"'
assert initials("  june  ") == "J", "extra spaces should be ignored"
assert initials("Cher") == "C", "one word gives one letter"
assert initials("") == "", 'empty text should give ""'
assert initials("   ") == "", 'only spaces should give ""'
print("All checks passed")
# ---- end of checks ----
