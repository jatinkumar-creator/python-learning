t = (1, 2, 3)
print(t[0], t[-1], t[1:])

try:
    t[0] = 10
except TypeError as e:
    print("TypeError:", e)

print(type((5)), type((5,)), type(()))    # the comma makes the tuple

a, b, c = t                               # unpacking
first, *rest = [1, 2, 3, 4, 5]
print(a, b, c, first, rest)

def min_max(nums):
    return min(nums), max(nums)           # returns a tuple

lo, hi = min_max([4, 9, 1, 7])
print(lo, hi)

# immutability is shallow
t2 = ([1, 2], 3)
t2[0].append(99)
print(t2)

# tuples as dict keys
points = {(0, 0): "origin", (1, 2): "point A"}
print(points[(1, 2)])

# namedtuple
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(3, 4)
print(p.x, p.y, p, (p.x ** 2 + p.y ** 2) ** 0.5)