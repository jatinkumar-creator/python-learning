t = (1, 2, 3)
single = (5,)
packed = 1, 2, 3
empty = ()
print(type((5)), type(single), type(packed), type(empty))
print(tuple("abc"), tuple([1, 2]), tuple(range(3)))

# Accessing
print(t[0], t[-1], t[1:], t[::-1], len(t))
for item in t:
    print(item, end=" ")
print()
print(t.count(2), t.index(3), 2 in t)

# Immutability
try:
    t[0] = 10
except TypeError as err:
    print("TypeError:", err)

print(t + (4,), t * 2)             # new tuples, t itself is unchanged
t2 = t + (4,)
print(t, t2)

# Immutability is shallow
inner = ([1, 2], 3)
inner[0].append(99)
print(inner)
try:
    hash(inner)
except TypeError as err:
    print("TypeError:", err)

# Unpacking and swapping
a, b, c = t
first, *rest = (1, 2, 3, 4)
x, y = 1, 2
x, y = y, x
print(a, b, c, first, rest, x, y)

# Tuples as dict keys, and as return values
grid = {(0, 0): "origin", (1, 2): "A"}
print(grid[(1, 2)])

def min_max(nums):
    return min(nums), max(nums)

print(min_max([4, 9, 1, 7]))

from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(3, 4)
print(p.x, p.y, p, p[0])

import sys
print(sys.getsizeof([1, 2, 3]), sys.getsizeof((1, 2, 3)))