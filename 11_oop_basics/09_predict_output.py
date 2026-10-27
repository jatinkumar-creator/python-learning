# 1
class A:
    x = 1
a = A()
a.x = 2
print(A.x, a.x)

# 2
class A:
    items = []
a, b = A(), A()
a.items.append(1)
print(b.items)

# 3
class A:
    def __init__(self):
        self.v = 1
a = A()
b = a
b.v = 5
print(a.v)

# 4
class P:
    def __init__(self, x):
        self.x = x
print(P(1) == P(1))

# 5
class A:
    def __repr__(self):
        return "A-repr"
    def __str__(self):
        return "A-str"
print(A(), [A()], str(A()), repr(A()))

# 6
class A:
    def hi(self):
        return "hi"
a = A()
print(A.hi(a), a.hi(), type(a.hi).__name__, type(A.hi).__name__)

# 7
class A:
    x = 1
a = A()
a.x = 2
del a.x
print(a.x)

# 8
class Counter:
    n = 0
    def bump(self):
        self.n += 1
c = Counter()
c.bump()
c.bump()
print(c.n, Counter.n)

# 9
class P:
    def __init__(self, tags=[]):
        self.tags = tags
a, b = P(), P()
a.tags.append("x")
print(b.tags)

# 10
class A:
    pass
print(type(A), type(A()), A.__name__, isinstance(A(), object))

# 11
class V:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
print(V(1) == V(1), V(1) != V(2))
try:
    hash(V(1))
except TypeError:
    print("unhashable")

# 12
class A:
    count = 0
    def __init__(self):
        A.count += 1
x, y, z = A(), A(), A()
print(A.count, x.count)