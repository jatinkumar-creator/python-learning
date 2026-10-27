from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    def describe(self):                     # a concrete method, shared by every child
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

try:
    Shape()
except TypeError as e:
    print("TypeError:", e)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)

class Incomplete(Shape):                    # implements only one of the two
    def area(self):
        return 0

try:
    Incomplete()
except TypeError as e:
    print("TypeError:", e)

for s in (Circle(1), Rectangle(3, 4)):
    print(s.describe())

# An abstract property
class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self):
        ...

class Car(Vehicle):
    @property
    def wheels(self):
        return 4

print(Car().wheels)

# An abstract method may still have a body that children can call
class Base(ABC):
    @abstractmethod
    def greet(self):
        return "default greeting"

class Child(Base):
    def greet(self):
        return super().greet() + " (customised)"

print(Child().greet())

# Two traps
class Plain(ABC):                           # no abstract methods, so it CAN be instantiated
    pass
print(Plain())

class NotReallyAbstract:                    # no ABC base: @abstractmethod is NOT enforced
    @abstractmethod
    def f(self):
        ...
print(NotReallyAbstract())

print(isinstance(Circle(1), Shape), issubclass(Rectangle, Shape))
print(Shape.__abstractmethods__)