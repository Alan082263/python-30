# Day 3, Problem 2: Vowels, and hiding an email address
#
# Part A. count_vowels(text) -> how many of a e i o u are in the text.
#   This is your vowel counter, fixed: capitals must count too.
#   "HELLO" -> 2,  "Why?" -> 0,  "AEIOUaeiou" -> 10
#   Hint: make a lowercase copy first, then loop over it with `for ch in ...`.
#
# Part B. mask_email(email) -> the email with most of the name hidden:
#   "alan@example.com" -> "a***@example.com"
#   Keep the first character, then three stars, then everything from the @ onward.
#   If there is no @, or the @ is the very first character (nothing before it), return None.
#   Hint: text.find("@") gives the position, or -1 if it's missing.
#   Use slicing: email[:1] is the first character, email[at:] is from the @ to the end.

vowels = ["a","e","i","o","u"]

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count


def mask_email(email):
    at = email.find("@")
    if at <= 0:
        return None
    return email[:1] + "***" + email[at:]



# ---- checks: don't edit this part ----
assert count_vowels("hello") == 2, '"hello" has 2 vowels'
assert count_vowels("HELLO") == 2, 'capitals count too: "HELLO" has 2 vowels'
assert count_vowels("Why?") == 0, '"Why?" has no vowels'
assert count_vowels("AEIOUaeiou") == 10, "all ten should be counted"
assert count_vowels("") == 0, "empty text has no vowels"

assert mask_email("alan@example.com") == "a***@example.com", "keep first letter, hide the rest"
assert mask_email("b@x.ca") == "b***@x.ca", "one-letter names work too"
assert mask_email("no-at-sign") is None, "no @ should give None"
assert mask_email("@x.ca") is None, "nothing before the @ should give None"
assert mask_email("") is None, "empty text should give None"
print("All checks passed")
# ---- end of checks ----


# Your program goes here:
# Ask "Enter an email: ". Print the masked version, or "That doesn't look like an email."
# if mask_email gave back None. Run it again for each of: alan@example.com, hello, @oops.

email = input("Enter your email: ").strip()

masked = mask_email(email)


if masked is None:
    print("That doesn't look like an email.")
else:
    print(masked)
