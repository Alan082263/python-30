# Day 3, Problem 3: Fix the bugs
#
# Each function below has ONE bug, and each bug is one of today's gotchas.
# First read the code and try to spot each bug without running anything.
# Then run the file: the checks will tell you which ones still fail.
#
# Rules: fix the functions only. Don't edit the checks at the bottom.
#
#   shout(text)        -> text with spaces trimmed, UPPERCASE, and "!" added: "  hello " -> "HELLO!"
#   last_char(text)    -> the last character of the text: "python" -> "n"
#   contains_at(text)  -> True if the text has an "@" anywhere in it, otherwise False


def shout(text):
    return text.strip().upper() + "!"    #SHOUT


def last_char(text):     #Last Char
    return text[-1]


def contains_at(text):      #contains_@
    return "@" in text



# ---- checks: don't edit this part ----
assert shout("  hello ") == "HELLO!", 'shout("  hello ") should be "HELLO!"'
assert shout("hi") == "HI!", 'shout("hi") should be "HI!"'

assert last_char("python") == "n", 'last_char("python") should be "n"'
assert last_char("a") == "a", 'last_char("a") should be "a"'

assert contains_at("a@b") is True, '"a@b" has an @'
assert contains_at("@home") is True, '"@home" has an @, even at position 0'
assert contains_at("abc") is False, '"abc" has no @'
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write a comment here (one line each) saying what each bug was.
