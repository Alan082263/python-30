# Day 8, Problem 1: Predict the output
#
# Closed book. DO NOT RUN THIS FILE until you've written all eight predictions below.
#
# Read the code, then write what each numbered print line will show, exactly as it would
# appear on screen. If a line shows a special value, write that, e.g. None.
# The file has 8 print lines, so it will produce 8 lines of output.
# Lines that print several values put a space between them.
#
# MY PREDICTIONS (fill these in):
#   1: (18, 3)
#   2:b {'a': 3, 'b': 1, 'c': 1}
#   3:[3,1,2,9]
#   4: None [1,2,3,9]
#   5: {2, 3} 2
#   6: 0 True False
#   7: 2 1 5 (5,)
#   8: [1, 2]
#
# Then run the file and compare. Score one point per line you got exactly right.


def total_and_count(numbers):
    return sum(numbers), len(numbers)


def tally(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def without_repeats(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


print(total_and_count([4, 6, 8]))                              # 1 (18, 3)
print(tally(["a", "b", "a", "c", "a"]))                        # 2 {'a': 3, 'b': 1, 'c': 1}

a = [3, 1, 2]
b = a
b.append(9)
print(a)                                                       # 3 [3,1,2,9]
result = a.sort()
print(result, a)                                               # 4 None [1,2,3,9]

print({1, 2, 3} & {2, 3, 4}, len({1, 1, 2}))                   # 5 {2, 3} 2

prices = {"tea": 2, "milk": 3}
print(prices.get("coffee", 0), "tea" in prices, 2 in prices)   # 6 0 True False

x, y = (1, 2)
x, y = y, x
print(x, y, (5), (5,))                                         # 7 2 1 5 (5,)

print(without_repeats([3, 1, 3, 2, 1])[1:])                    # 8 [1, 2]
