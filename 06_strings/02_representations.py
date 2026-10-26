# Escape sequences
print("Line1\nLine2")
print("Tab\there")
print("Backslash: \\")
print("Quotes: \" and \'")

# Raw strings
print("C:\new\table")              # \n and \t are interpreted
print(r"C:\new\table")             # raw: backslashes stay literal
print(len(r"a\nb"), len("a\nb"))

# str() vs repr()
s = "Hi\n"
print(str(s))
print(repr(s))
print([s])                         # containers show items with repr
name = "Asha"
print(f"{name!r} {name!s}")

# bytes literal
b = b"abc"
print(b, type(b), b[0])

# repr/str on your own class
class Point:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return f"Point(x={self.x!r})"
    def __str__(self):
        return f"Point with x={self.x}"

p = Point(5)
print(p)
print([p])
print(repr(p))