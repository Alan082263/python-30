# Day 1, Problem 1: Temperature converters
#
# Write two functions. Each one RETURNS its answer; neither one prints.
#
#   to_fahrenheit(c)  ->  the temperature in degrees Fahrenheit
#   to_celsius(f)     ->  the temperature in degrees Celsius
#
# Formulas:  F = C * 9/5 + 32        C = (F - 32) * 5/9
#
# Then, at the bottom of the file, write a small program that asks the user
# for a temperature in Celsius, calls to_fahrenheit, and prints the answer
# in a sentence (use an f-string, rounded to 1 decimal place).


def to_fahrenheit(c):
    return c * 9/5 + 32


def to_celsius(f):
    return (f - 32) * 5/9


# ---- checks: don't edit this part ----
assert to_fahrenheit(0) == 32, "0 C should be 32 F"
assert to_fahrenheit(100) == 212, "100 C should be 212 F"
assert to_fahrenheit(-40) == -40, "-40 C should be -40 F"
assert to_celsius(212) == 100, "212 F should be 100 C"
assert round(to_celsius(98.6), 1) == 37.0, "98.6 F should be 37.0 C"
print("All checks passed")
# ---- end of checks ----


# Your interactive program goes here:
celsius = float(input("Enter a temperature in Celsius: "))

fahrenheit = to_fahrenheit(celsius)

print(f"{celsius}°C is {fahrenheit:.1f}°F")
