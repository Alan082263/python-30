# Day 4, Problem 2: Find and fix the bugs
#
# Closed book. This function has TWO bugs. Fix the function only; don't edit the checks.
#
#   parse_percent(text) -> a float from 0 to 100 (inclusive) if the text is a percentage,
#                          otherwise None.
#                          The text may have spaces around it and may end with a % sign:
#                          " 45.5% " -> 45.5,   "100" -> 100.0,   "abc" -> None
#
# Read the code first and try to spot the bugs by thinking, then run the checks.
import math
def parse_percent(text):
    text = text.strip().removesuffix("%")

    try:
        value = float(text)
    except ValueError:
        return None
    if not math.isfinite(value) or value < 0 or value > 100:
        return None
    return value


# ---- checks: don't edit this part ----
assert parse_percent("45.5") == 45.5, '"45.5" should be 45.5'
assert parse_percent("45.5%") == 45.5, '"45.5%" should be 45.5'
assert parse_percent(" 45.5% ") == 45.5, "spaces around the text should be fine"
assert parse_percent("100%") == 100.0, '"100%" is allowed (the top)'
assert parse_percent("0") == 0.0, '"0" is allowed (the bottom)'
assert parse_percent("101") is None, '"101" is too big'
assert parse_percent("-1%") is None, '"-1%" is too small'
assert parse_percent("abc") is None, '"abc" is not a number'
assert parse_percent("") is None, "empty text is not a number"
assert parse_percent("%") is None, 'just "%" is not a number'
assert parse_percent("nan") is None, '"nan" is not a real number'
assert parse_percent("inf") is None, '"inf" is not a real number'
print("All checks passed")
# ---- end of checks ----

# When all checks pass, write one comment line here for each bug, saying what it was.
# Bug: Non-numeric input could raise ValueError instead of returning None.
# Bug: Values outside the 0–100 range were not rejected.
# Bug: NaN and infinity needed to be rejected as non-finite values.
# Bug: A trailing percent sign needed to be removed before converting the text to a number.
