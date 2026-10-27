class Animal:                                  # a base class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):                             # INHERITANCE: Dog reuses Animal
    def speak(self):                           # POLYMORPHISM: same method name, different behaviour
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Wallet:
    def __init__(self, cash):
        self._cash = cash                      # ENCAPSULATION: internal data (underscore = "keep out")

    def spend(self, amount):                   # ABSTRACTION: callers use spend(), not the internals
        if amount > self._cash:
            return "Not enough cash"
        self._cash -= amount
        return self._cash

for pet in [Dog("Rex"), Cat("Tom"), Animal("Thing")]:
    print(pet.speak())

w = Wallet(100)
print(w.spend(30), w.spend(500))
print(isinstance(Dog("Rex"), Animal), issubclass(Cat, Animal))