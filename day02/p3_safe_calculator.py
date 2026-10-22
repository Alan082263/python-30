# Day 2, Problem 3: A calculator that can't be crashed
#
# This is your calc.py rebuilt properly. parse_number is provided (it's yesterday's
# idea from Problem 1). You write calculate, then the program at the bottom.
#
#   calculate(a, op, b)  ->  the result of a op b, where op is one of + - * /
#
# New idea: raise. A function can stop and report a problem by raising an error:
#
#       raise ValueError("Something went wrong.")
#
# The caller catches it with try/except ValueError as e, and e holds the message.
#
# calculate must raise ValueError in two cases:
#   - the operator isn't one of + - * /   -> message "Invalid operator."
#   - dividing by zero                    -> message "Cannot divide by zero."
#
# Program at the bottom:
#   1. Ask for the first number, repeating until it's valid.
#   2. Ask for the second number, repeating until it's valid.
#   3. Ask for the operator, repeating until it's one of + - * /
#   4. Call calculate inside try/except ValueError and print the result,
#      or print the error message.
#   5. Ask "Another? (y/n): ". If the answer is y, go again. Anything else, stop.


def parse_number(text):
    try:
        return float(text)
    except ValueError:
        return None


def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operator.")




# ---- checks: don't edit this part ----
def raises_value_error(a, op, b):
    try:
        calculate(a, op, b)
    except ValueError:
        return True
    return False


assert calculate(2, "+", 3) == 5, "2 + 3 should be 5"
assert calculate(2, "-", 3) == -1, "2 - 3 should be -1"
assert calculate(2, "*", 3) == 6, "2 * 3 should be 6"
assert calculate(7, "/", 2) == 3.5, "7 / 2 should be 3.5"
assert raises_value_error(1, "/", 0), "1 / 0 should raise ValueError"
assert raises_value_error(1, "^", 2), "operator ^ should raise ValueError"
assert not raises_value_error(0, "/", 5), "0 / 5 is fine and should not raise"
print("All checks passed")
# ---- end of checks ----


# Your calculator program goes here:
num1 = float(input("Enter a valid number: "))
num2 = float(input("Enter a second valid number: "))
op = (input("Enter an operator (+, -, *, /): ").strip())
