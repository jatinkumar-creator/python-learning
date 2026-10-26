s = "Python"
print(s[0], s[-1], s[1:4], s[::-1], len(s))

try:
    s[0] = "J"
except TypeError as e:
    print("TypeError:", e)

print("J" + s[1:])                       # build a new string instead
print(s.upper(), s.find("th"), s.replace("P", "J"))
print("-".join(["a", "b", "c"]), "a,b,c".split(","))
print(s, id(s))
s += "!"
print(s, id(s))                          # a different object: strings are immutable