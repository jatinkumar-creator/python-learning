s = "Python"
print(type(s), len(s))
print(type(s[0]))                  # no char type: a 1-character str

# Ways to write strings
a = 'single'
b = "double"
c = '''triple
single'''
d = """triple
double"""
print(a, b, c, d, sep=" | ")
print("it's", 'He said "hi"')
print("Py" "thon")                 # adjacent literals are joined

# Truthiness
print(bool(""), bool("0"), bool("False"), bool(" "))

# Immutability
try:
    s[0] = "J"
except TypeError as e:
    print("TypeError:", e)

t = s.upper()
print(s, t, s is t)                # the original is unchanged
print(id(s))
s += "!"
print(id(s))                       # a new object