class Temperature:
    unit = "C"

    def __init__(self, degrees):
        self.degrees = degrees

    def to_fahrenheit(self):                 # instance method: receives the object (self)
        return self.degrees * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f):             # class method: receives the class (cls)
        return cls((f - 32) * 5 / 9)

    @classmethod
    def describe(cls):
        return f"Temperatures in {cls.unit}"

    @staticmethod
    def is_valid(degrees):                   # static method: receives nothing automatically
        return degrees >= -273.15

t = Temperature(100)
print(t.to_fahrenheit())
print(Temperature.from_fahrenheit(212).degrees)      # an alternative constructor
print(Temperature.describe(), t.describe())
print(Temperature.is_valid(-300), t.is_valid(20))

# Another alternative constructor
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name.strip(), int(age))

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

print(Person.from_string("Asha, 28"))

# Which is which?
print(type(t.to_fahrenheit).__name__, type(Temperature.to_fahrenheit).__name__)
print(type(Temperature.from_fahrenheit).__name__, type(Temperature.is_valid).__name__)