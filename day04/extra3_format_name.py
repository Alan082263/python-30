# Extra practice 3: The same shape as p3, with less help
#
# OPEN BOOK. This is close to make_username, so if you do it, p3 will be much easier.
# Do the steps in order and print after each one. Write your own comments first.
#
# Write the function:
#
#   format_name(full_name)  -> the name as "Last, First", each with a capital first letter.
#                              "Alan Wade"               -> "Wade, Alan"
#                              "alan george WADE"        -> "Wade, Alan"   (middle name ignored)
#                              "  alan   wade  "         -> "Wade, Alan"   (extra spaces ignored)
#                              "cher"                    -> "Cher"         (one word: just it, capitalized)
#
#   If the name is empty or only spaces, RAISE a ValueError with the message "Name is empty."
#
# Useful pieces:
#   words[0]          the first word          words[-1]   the last word
#   word.capitalize() makes "ALAN" or "alan" into "Alan"
#   f"{a}, {b}"       puts a comma and space between two values
#
# Plan it as comments first (4 or 5 steps), like the recipe in the problem workflow:
#   1. split into words
#   2. no words? raise
#   3. one word? return it, capitalized
#   4. otherwise return the last word and first word in the "Last, First" shape


def format_name(full_name):
    #   1. split into words
    name = full_name.split()
    #2. no words? raise
    if len(name) == 0:
        raise ValueError("Name is empty.")
    #3. one word? return it, capitalized
    elif len(name) == 1:
        return name[0].capitalize()
    #4. otherwise return the last word and first word in the "Last, First" shape
    else:
        first = name[0].capitalize()
        last = name[-1].capitalize()
        return f"{last}, {first}"


# ---- checks: don't edit this part ----
def raises_value_error(text):
    try:
        format_name(text)
    except ValueError:
        return True
    return False


assert format_name("Alan Wade") == "Wade, Alan", '"Alan Wade" should give "Wade, Alan"'
assert format_name("alan george WADE") == "Wade, Alan", "middle names ignored, capitals fixed"
assert format_name("  alan   wade  ") == "Wade, Alan", "extra spaces ignored"
assert format_name("cher") == "Cher", 'one word "cher" should give "Cher"'
assert raises_value_error(""), "empty text should raise ValueError"
assert raises_value_error("   "), "only spaces should raise ValueError"
try:
    format_name("")
except ValueError as e:
    assert str(e) == "Name is empty.", 'the message should be "Name is empty."'
print("All checks passed")
# ---- end of checks ----
