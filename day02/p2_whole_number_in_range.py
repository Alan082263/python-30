# Day 2, Problem 2: A whole number within limits
#
# Write the function:
#
#   parse_whole_number(text, low, high)
#       -> the text as an int if it is a whole number from low to high (inclusive),
#          otherwise None
#
# Use try/except ValueError, then check the range. Notice that int("2.5") raises
# ValueError, so decimals should come back as None without any extra code.
#
# Then, at the bottom, write a program that asks "Pick a number from 1 to 10: ".
# The user gets at most 3 attempts.
#   - Valid entry: print "Got it: 7" (with their number) and stop asking.
#   - After 3 bad entries: print "Too many tries."
# Count the attempts with a variable and a while loop.


def parse_whole_number(text, low, high):
    try:
            value = int(text)
    except ValueError:
            return None

    if low <= value <= high:
            return value
    else:
        return None


# ---- checks: don't edit this part ----
assert parse_whole_number("5", 1, 10) == 5, '"5" in 1-10 should be 5'
assert parse_whole_number("1", 1, 10) == 1, '"1" is allowed (lowest)'
assert parse_whole_number("10", 1, 10) == 10, '"10" is allowed (highest)'
assert parse_whole_number(" 7 ", 1, 10) == 7, "spaces around the number should be fine"
assert parse_whole_number("0", 1, 10) is None, '"0" is below the range'
assert parse_whole_number("11", 1, 10) is None, '"11" is above the range'
assert parse_whole_number("abc", 1, 10) is None, '"abc" is not a number'
assert parse_whole_number("2.5", 1, 10) is None, '"2.5" is not a whole number'
assert parse_whole_number("", 1, 10) is None, "empty text should be None"
print("All checks passed")
# ---- end of checks ----


# Your 3-attempt program goes here:
attempts = 0
max_attempts = 3
picked = None

while attempts < max_attempts:
    guess = input("Pick a number between 1-10: ")
    attempts += 1

    try:
        guess = int(guess)

    except ValueError:
        print("Please print a whole number: ")
        continue

    if not 1 <= guess  <=10:
        print("Please pick anumber between 1 and 10: ")
        continue

    picked = guess
    print(f"Got it! {guess}.")
    break

if picked is None:
    print("Too many attempts.")
