import math
from functools import singledispatch

# 1. Polymorphism through overriding
class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s ** 2

class Triangle(Shape):
    def __init__(self, b, h):
        self.b, self.h = b, h
    def area(self):
        return 0.5 * self.b * self.h

for s in [Circle(1), Square(2), Triangle(3, 4)]:
    print(f"{type(s).__name__:<10}{s.area():.2f}")      # the caller never checks the type

try:
    Shape().area()
except NotImplementedError as e:
    print("NotImplementedError:", e)

# 2. Duck typing: "if it quacks like a duck..." (no shared parent needed)
class Duck:
    def speak(self):
        return "Quack"

class Robot:
    def speak(self):
        return "Beep"

class Rock:
    pass

def make_it_speak(thing):
    return thing.speak()

print([make_it_speak(x) for x in (Duck(), Robot())])
try:
    make_it_speak(Rock())
except AttributeError as e:
    print("AttributeError:", e)

# 3. Built-in polymorphism
print(len("abc"), len([1, 2]), len({"a": 1}), len(range(5)))
print(1 + 2, "a" + "b", [1] + [2], (1,) + (2,))
print(2 * 3, "ab" * 3, [0] * 3)
print(sorted([3, 1, 2]), sorted("bca"), sorted({"b": 1, "a": 2}))

# 4. Python has NO method overloading: the last definition wins
class Calc:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c

try:
    Calc().add(1, 2)
except TypeError as e:
    print("TypeError:", e)
print(Calc().add(1, 2, 3))

class Calc2:
    def add(self, *nums):                   # one flexible method instead
        return sum(nums)

print(Calc2().add(1, 2), Calc2().add(1, 2, 3, 4))

# 5. Dispatching on the argument's type
@singledispatch
def describe(x):
    return f"something else: {x!r}"

@describe.register
def _(x: int):
    return f"an int: {x}"

@describe.register
def _(x: str):
    return f"a string of length {len(x)}"

@describe.register(list)
def _(x):
    return f"a list of {len(x)} items"

print(describe(5), describe("hi"), describe([1, 2]), describe(3.5), sep="\n")