class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def eat(self):
        return f"{self.name} eats"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)             # run the parent's __init__
        self.breed = breed

    def speak(self):                       # overriding: replaces the parent's version
        return f"{self.name} says Woof"

    def fetch(self):                       # a new method only Dog has
        return f"{self.name} fetches"

d = Dog("Rex", "Labrador")
print(d.speak())
print(d.eat())                             # inherited, not redefined
print(d.fetch())
print(d.__dict__)

print(isinstance(d, Dog), isinstance(d, Animal), isinstance(d, object))
print(issubclass(Dog, Animal), issubclass(Animal, Dog))
print(type(d) is Animal, type(d).__name__)
print(Dog.__bases__)

try:
    Animal("Thing").fetch()
except AttributeError as e:
    print("AttributeError:", e)

# Forgetting super().__init__()
class Cat(Animal):
    def __init__(self, name):
        self.lives = 9                     # the parent's __init__ never ran

c = Cat("Tom")
try:
    print(c.name)
except AttributeError as e:
    print("AttributeError:", e)

# Extending (not replacing) a parent method
class Puppy(Dog):
    def speak(self):
        return super().speak() + " (squeakily)"

print(Puppy("Bit", "Pug").speak())