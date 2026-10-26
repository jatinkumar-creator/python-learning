# Trap 1: the result is discarded
s = "hello"
s.upper()
print(s)
s = s.upper()
print(s)

# Trap 2: find() returns 0 for a match at the start
word = "hello"
if word.find("h"):
    print("found (this line does NOT print)")
if "h" in word:
    print("found with 'in'")

# Trap 3: strip removes a SET of characters, not a substring
print("hello".strip("hel"))
print("hello".removeprefix("hel"))

# Trap 4: split() vs split(" ")
print("a  b".split())
print("a  b".split(" "))

# Trap 5: title() and apostrophes
print("it's".title())
import string
print(string.capwords("it's"))

# Trap 6: isdigit is not a number check
for text in ["12", "-5", "3.5", "²"]:
    print(repr(text), text.isdigit())

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

print(is_number("3.5"), is_number("-7"), is_number("abc"))

# Trap 7: join needs strings
try:
    print(",".join([1, 2, 3]))
except TypeError as e:
    print("TypeError:", e)