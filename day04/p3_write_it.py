# Day 4, Problem 3: Write it from scratch
#
# Closed book. Write the whole function body yourself; there is no hint code.
#
#   make_username(full_name) -> a username built from a person's name:
#       the first letter of the FIRST word + the LAST word, all lowercase, no spaces.
#
#       "Alan Wade"                  -> "awade"
#       "  alan   george  WADE "     -> "awade"     (extra spaces ignored, middle names ignored)
#       "Cher"                       -> "cher"      (one word: just that word in lowercase)
#
#   If the name is empty, or only spaces, raise ValueError with the message "Name is empty."
#
# The function must return its answer, not print it.

def make_username(full_name):
#   1. split into words
    username = full_name.split()

    #2. no words? raise
    if len(username) == 0:
        raise ValueError("Name is empty.")
    elif len(username) == 1:
        return username[0].lower()
    else:
        return (username[0][0].lower()) + (username[-1].lower())







# ---- checks: don't edit this part ----
def raises_value_error(text):
    try:
        make_username(text)
    except ValueError:
        return True
    return False


assert make_username("Alan Wade") == "awade", '"Alan Wade" should give "awade"'
assert make_username("  alan   george  WADE ") == "awade", "extra spaces and middle names ignored"
assert make_username("Cher") == "cher", 'one word "Cher" should give "cher"'
assert make_username("JUNE SMITH") == "jsmith", "capitals should be lowercased"
assert raises_value_error(""), "empty text should raise ValueError"
assert raises_value_error("   "), "only spaces should raise ValueError"
assert not raises_value_error("Bo"), "a one-word name is fine"
try:
    make_username("")
except ValueError as e:
    assert str(e) == "Name is empty.", 'the message should be "Name is empty."'
print("All checks passed")
# ---- end of checks ----
