s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[0], s[5], s[-1], s[-6])

try:
    print(s[6])
except IndexError as e:
    print("IndexError:", e)

# Slices: predict each first
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[-3:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[4:1:-1])
print(s[10:20] == "")
print(s[2:2] == "")
print(s[-100:100])

try:
    print(s[1:4:0])
except ValueError as e:
    print("ValueError:", e)

print(s[:3] + s[3:] == s)

# "Changing" a character by rebuilding
print(s[:2] + "X" + s[3:])

# Iteration
for i, ch in enumerate("abc"):
    print(i, ch)