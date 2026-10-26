import keyword

# Character set: Python 3 source is Unicode (UTF-8)
name = "Jatin"            # a Unicode identifier (legal in Python 3)
cafe = 5
print(name, cafe)

# Escape sequences
print("Line1\nLine2")
print("Tab\there")
print("Backslash: \\")
print("Quote: \" and \'")
print("Unicode: \u00e9 \u0905")
print("Emoji: \U0001F600")

# Keywords
print(len(keyword.kwlist))
print(keyword.kwlist)
print(keyword.iskeyword("class"), keyword.iskeyword("print"))

# A comment explains WHY, not what
x = 10   # inline comment