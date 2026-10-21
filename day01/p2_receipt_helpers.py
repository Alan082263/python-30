# Day 1, Problem 2: Receipt helpers
#
# Write three functions. All of them RETURN their answer; none of them print.
#
#   add_tax(subtotal, rate)   ->  the subtotal plus tax, e.g. add_tax(100, 0.12) is 112
#   format_money(amount)      ->  a string with a dollar sign and 2 decimals,
#                                 e.g. format_money(4.5) is "$4.50"
#   receipt_line(name, price) ->  a string like "Milk: $4.50"
#
# Rule: receipt_line must CALL format_money, not repeat its formatting code.
# That is the point of the exercise: functions that use other functions.
#
# Then, at the bottom, use all three to print a short receipt for these items,
# with 12% tax (GST + PST in BC) added to the total:

names = ["Milk", "Bread", "Eggs"]
prices = [4.50, 3.25, 5.99]


def add_tax(subtotal, rate):
    return   subtotal * (1 + rate) # replace this line


def format_money(amount):
    return f"${amount:.2f}"  # replace this line


def receipt_line(name, price):
    return f"{name}: {format_money(price)}" # replace this line


# ---- checks: don't edit this part ----
answer = add_tax(100, 0.12)
assert answer is not None, "add_tax gave back nothing (None). Did you forget return?"
assert round(answer, 2) == 112.0, "100 plus 12% tax should be 112"
answer = add_tax(0, 0.12)
assert answer is not None, "add_tax gave back nothing (None). Did you forget return?"
assert round(answer, 2) == 0.0, "0 plus tax should be 0"
assert format_money(4.5) == "$4.50", "4.5 should become $4.50"
assert format_money(0) == "$0.00", "0 should become $0.00"
assert receipt_line("Milk", 4.5) == "Milk: $4.50", "receipt_line should give Milk: $4.50"
print("All checks passed")
# ---- end of checks ----


# Your receipt program goes here:
print("\nRECEIPT")
print("-------")

subtotal = 0

for name, price in zip(names, prices):
    print(receipt_line(name, price))
    subtotal += price

print("-------")
print(f"Subtotal: {format_money(subtotal)}")

total = add_tax(subtotal, 0.12)

print(f"Total with tax: {format_money(total)}")
