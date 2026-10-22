# Day 2, Problem 1: parse_number
#
# Write the function:
#
#   parse_number(text)  ->  the text as a float, or None if it isn't a number
#
# Use try/except ValueError. The function returns; it does not print.
#
# Then, at the bottom, write a program that keeps asking "Enter a number: " until
# the user types a valid one, then prints double that number, e.g. "Double is 9.0".
# If the entry is bad, print a short message and ask again.
#
# Stretch: float("nan") and float("inf") are accepted by Python. Make parse_number
# reject them too (return None). Hint: look up math.isfinite.

import math

def parse_number(text):
    try:
        value = float(text)
    except ValueError:
        return None

    if math.isfinite(value):
        return value
    else:
        return None


# ---- checks: don't edit this part ----
assert parse_number("3") == 3.0, 'parse_number("3") should be 3.0'
assert parse_number("4.5") == 4.5, 'parse_number("4.5") should be 4.5'
assert parse_number(" 4.5 ") == 4.5, "spaces around the number should be fine"
assert parse_number("-2") == -2.0, 'parse_number("-2") should be -2.0'
assert parse_number("abc") is None, 'parse_number("abc") should be None'
assert parse_number("") is None, 'parse_number("") should be None'
assert parse_number("1,5") is None, 'parse_number("1,5") should be None'
assert parse_number("12abc") is None, 'parse_number("12abc") should be None'
print("All checks passed")
# ---- end of checks ----


# Your loop goes here:
while True:
    number = input("Enter a valid number: ")
    result = parse_number(number)

    if result is not None:
        break

    print("Invalid input. Please try again.")

print(f"Double is {result * 2}")
