a = [1, 2, 3]
b = list("abc")
c = list(range(5))
empty = []
zeros = [0] * 3
mixed = [1, "two", 3.0, [4, 5], None]
print(a, b, c, empty, zeros, mixed, sep="\n")
print(len(mixed), type(mixed))

# Accessing
print(a[0], a[-1], mixed[3][1])
for x in a:
    print(x, end=" ")
print()
for i, ch in enumerate(b):
    print(i, ch)
print(3 in a, 9 not in a)

try:
    print(a[10])
except IndexError as err:
    print("IndexError:", err)

# Changing items (lists are mutable)
a[0] = 100
print(a)
del a[1]
print(a)