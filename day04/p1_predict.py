# Day 4, Problem 1: Predict the output
#
# Closed book. DO NOT RUN THIS FILE until you've written all eight predictions below.
#
# Read the code, then write what each numbered print line will show, exactly as it would
# appear on screen. If a line shows nothing or a special value, write that, e.g. None.
# Remember: the file has 8 print lines, so it will produce 8 lines of output.
#
# MY PREDICTIONS (fill these in):
#   1:
#   2:
#   3:
#   4:
#   5:
#   6:
#   7:
#   8:
#
# Then run the file and compare. Score one point per line you got exactly right.


def mystery(text):
    cleaned = text.strip().lower()
    return cleaned[::-1][:3]


def check(value):
    try:
        number = float(value)
    except ValueError:
        return None
    if number > 10:
        return "big"
    return number


def count_up(limit):
    total = 0
    n = 0
    while True:
        n += 1
        if n % 2 == 0:
            continue
        if n > limit:
            break
        total += n
    return total


def shout(text):
    text.upper()
    return text + "!"


print(mystery("  PyThon "))                  # 1
print(check("12"))                           # 2
print(check("3.5"))                          # 3
print(check("abc"))                          # 4
print(count_up(6))                           # 5
print(shout("hi"))                           # 6
print("hello"[1:4], "hello"[-2:])            # 7  (two values: print puts a space between)
print("banana".find("z"), "banana".find("n"))  # 8  (two values again)
