import json

# The diamond: D inherits from B and C, which both inherit from A
class A:
    def who(self):
        return ["A"]

class B(A):
    def who(self):
        return ["B"] + super().who()

class C(A):
    def who(self):
        return ["C"] + super().who()

class D(B, C):
    def who(self):
        return ["D"] + super().who()

print(D().who())
print([k.__name__ for k in D.__mro__])      # the Method Resolution Order

# Cooperative __init__: every class runs once, in MRO order
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        print("Left init")
        super().__init__()

class Right(Base):
    def __init__(self):
        print("Right init")
        super().__init__()

class Bottom(Left, Right):
    def __init__(self):
        print("Bottom init")
        super().__init__()

Bottom()

# Mixins: small classes that add one ability
class JsonMixin:
    def to_json(self):
        return json.dumps(vars(self))

class ReprMixin:
    def __repr__(self):
        args = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({args})"

class User(JsonMixin, ReprMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age

u = User("Asha", 28)
print(u.to_json())
print(u)

# An impossible ordering
class X:
    pass

class Y(X):
    pass

try:
    class Z(X, Y):
        pass
except TypeError as e:
    print("TypeError:", e)