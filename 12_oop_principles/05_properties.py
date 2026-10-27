class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius              # goes through the setter, so validation applies

    @property
    def celsius(self):                      # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):               # setter, with validation
        if not isinstance(value, (int, float)):
            raise TypeError("temperature must be a number")
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        print("deleting the temperature")
        del self._celsius

    @property
    def fahrenheit(self):                   # read-only, computed on demand
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(t.celsius, t.fahrenheit)
t.celsius = 100
print(t.fahrenheit)

for bad in (-300, "hot"):
    try:
        t.celsius = bad
    except (TypeError, ValueError) as e:
        print(type(e).__name__ + ":", e)

try:
    t.fahrenheit = 50
except AttributeError as e:
    print("AttributeError:", e)

try:
    Temperature(-500)
except ValueError as e:
    print("ValueError:", e)

print(type(Temperature.celsius), t.__dict__)
del t.celsius
print(hasattr(t, "_celsius"))

# A property that caches an expensive result
class Report:
    def __init__(self, data):
        self.data = data
        self._total = None

    @property
    def total(self):
        if self._total is None:
            print("calculating...")
            self._total = sum(self.data)
        return self._total

r = Report([1, 2, 3])
print(r.total, r.total)                     # "calculating..." appears only once