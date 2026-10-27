s = "hello"
print(len(s))                    # function: called on its own
print(s.upper())                 # method: belongs to the str object
print(str.upper(s))              # the same call written through the class
print(s.upper)                   # a bound method object
print(type(len).__name__, type(s.upper).__name__)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):              # a method: the first parameter is the instance
        return f"{self.name} says woof"

d = Dog("Rex")
print(d.bark())                  # Python passes d as self automatically
print(Dog.bark(d))               # the same thing, with self passed by hand
print(type(d.bark).__name__, type(Dog.bark).__name__)

m = d.bark                       # a bound method remembers its object
print(m())
print(m.__self__ is d, m.__func__ is Dog.bark)

def standalone(x):               # a plain function
    return x * 2
print(standalone(4))

class MathOps:
    @staticmethod
    def add(a, b):               # no self, no cls
        return a + b

    @classmethod
    def describe(cls):           # receives the class
        return cls.__name__

print(MathOps.add(1, 2), MathOps.describe())

try:
    Dog.bark()                   # forgot to pass the instance
except TypeError as e:
    print("TypeError:", e)