# Day 1, Problem 3: Fix the bugs
#
# Each function below is supposed to do what its comment says, and each one has a bug.
# Read it first. Predict what it does. Then run the file and see if you were right.
#
# Rules:
#   - Don't rewrite a function from scratch. Make the smallest change that fixes it.
#   - Above each fix, add a one-line comment saying what was wrong.


# Should return the sum of all the numbers in the list.
# Bug: return was inside the loop, so it stopped after the first number.
def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


# Should return the average of the numbers in the list.
# Bug: return was inside the loop, so it stopped after the first number.
def average(numbers):
    return sum(numbers) / len(numbers)
        #print(sum(numbers) / len(numbers))


# Should return the larger of a and b. If they are equal, return that value.
# Bug: equal case had no return, so it gave back None.
def biggest(a, b):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return a + b
def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


# Should return the average of the numbers in the list.
def average(numbers):
    return sum(numbers) / len(numbers)



# Should return the larger of a and b. If they are equal, return that value.
def biggest(a, b):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return a


# ---- checks: don't edit this part ----
assert total([1, 2, 3]) == 6, "total([1, 2, 3]) should be 6"
assert total([]) == 0, "total([]) should be 0"
assert average([2, 4]) == 3, "average([2, 4]) should be 3"
assert biggest(2, 9) == 9, "biggest(2, 9) should be 9"
assert biggest(9, 2) == 9, "biggest(9, 2) should be 9"
assert biggest(5, 5), "biggest(5, 5) should be 5"
print("All checks passed")
# ---- end of checks ----
