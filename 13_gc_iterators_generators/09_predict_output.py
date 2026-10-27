import gc
import sys

# 1
it = iter([1, 2])
print(next(it), next(it), next(it, "end"))

# 2
g = (x * x for x in range(3))
print(list(g), list(g))

# 3
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
print("created")
print(next(g))
print(next(g))

# 4
def f():
    return 1
    yield 2

print(type(f()).__name__, list(f()))

# 5
nums = [1, 2, 3]
it = iter(nums)
nums.append(4)
print(list(it))

# 6
it = iter([1])
print(iter(it) is it)

# 7
def counter():
    n = 0
    while True:
        n += 1
        yield n

c = counter()
print(next(c), next(c), next(c))

# 8
def g():
    yield from [1, 2]
    yield from "ab"

print(list(g()))

# 9
print(sys.getsizeof([x for x in range(1000)]) > sys.getsizeof((x for x in range(1000))))

# 10
class A:
    pass

a, b = A(), A()
a.o, b.o = b, a
del a, b
print(gc.collect() > 0)

# 11
def gen():
    x = yield 1
    print("got", x)
    yield 2

g = gen()
print(next(g))
print(g.send("hello"))

# 12
class Box:
    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        return iter(self.items)

b = Box()
print(list(b), list(b))

# 13
it = iter(range(3))
for x in it:
    if x == 1:
        break
print(list(it))

# 14
g = (i for i in range(3))
print(next(g), sum(g))

# 15
class Down:
    def __init__(self):
        self.n = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

d = Down()
print(list(d), list(d))