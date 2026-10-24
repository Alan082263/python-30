# Day 3, Problem 1: String toolkit
#
# Write three functions. Each one returns a value; none of them prints.
#
#   first_and_last(text)  -> the first and last characters joined: "python" -> "pn"
#                            A one-character string gives that character twice: "a" -> "aa"
#                            An empty string gives "".
#
#   is_palindrome(text)   -> True if the text reads the same forwards and backwards,
#                            ignoring upper/lower case and spaces.
#                            "Never odd or even" -> True,  "Python" -> False
#
#   clean_name(text)      -> tidy up a name someone typed:
#                            "  alan   WADE " -> "Alan Wade"
#                            Remove extra spaces and capitalize each word.
#
# Hints:
#   - text[0] and text[-1] pick out characters. Careful with the empty string!
#   - text[::-1] is the text reversed.
#   - text.split() with no argument breaks on any spaces and drops the empties.
#     " ".join(pieces) glues a list back together with single spaces.
#   - Remember: string methods return a NEW string. Keep the result.


def first_and_last(text):
    if text == "":
        return ""
    return text[0] + text[-1]



def is_palindrome(text):
    clean = "".join(text.lower().split())
    return clean == clean[::-1]



def clean_name(text):
    return " ".join(text.split()).title()


# ---- checks: don't edit this part ----
assert first_and_last("python") == "pn", '"python" should give "pn"'
assert first_and_last("ab") == "ab", '"ab" should give "ab"'
assert first_and_last("a") == "aa", '"a" should give "aa"'
assert first_and_last("") == "", 'empty text should give ""'

assert is_palindrome("racecar") is True, '"racecar" is a palindrome'
assert is_palindrome("Never odd or even") is True, "case and spaces should be ignored"
assert is_palindrome("Python") is False, '"Python" is not a palindrome'
assert is_palindrome("A") is True, "one letter is a palindrome"

assert clean_name("  alan   WADE ") == "Alan Wade", "extra spaces and caps should be tidied"
assert clean_name("june") == "June", "a single word should be capitalized"
assert clean_name("") == "", "empty text should give an empty string"
print("All checks passed")
# ---- end of checks ----


# Your program goes here:
# Ask "Enter your name: ", then print "Hello, Alan Wade!" using clean_name on what they typed.

name = input("Enter your name: ")
print(f"Hello, {clean_name(name)}!")
