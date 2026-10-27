class Account:
    def __init__(self, owner, balance):
        self.owner = owner                  # public
        self._bank = "ABC Bank"             # protected (convention)
        self.__balance = balance            # private (name-mangled)

    def get_balance(self):
        return self.__balance

a = Account("Asha", 100)
print(a.owner, a._bank, a.get_balance())

try:
    print(a.__balance)
except AttributeError as e:
    print("AttributeError:", e)

print(a.__dict__)                           # shows the mangled name
print(a._Account__balance)                  # still reachable: privacy is a convention
a._Account__balance = -999
print(a.get_balance())

# Name mangling and inheritance
class Parent:
    def __init__(self):
        self.__secret = "parent secret"
        self._shared = "protected value"

    def reveal(self):
        return self.__secret

class Child(Parent):
    def try_secret(self):
        try:
            return self.__secret            # becomes self._Child__secret
        except AttributeError as e:
            return f"AttributeError: {e}"

    def get_shared(self):
        return self._shared

c = Child()
print(c.reveal())
print(c.try_secret())
print(c.get_shared())
print(sorted(vars(c)))

# __slots__: fixes the attribute names, saves memory, blocks typos
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(1, 2)
try:
    p.z = 3
except AttributeError as e:
    print("AttributeError:", e)
print(hasattr(p, "__dict__"))