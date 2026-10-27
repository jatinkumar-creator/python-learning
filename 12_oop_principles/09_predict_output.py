from abc import ABC, abstractmethod

# 1
class A:
    def hi(self):
        return "A"
class B(A):
    pass
print(B().hi())

# 2
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        print("B init")
B()

# 3
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
B()

# 4
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

# 5
class A:
    def __init__(self):
        self.__x = 1
a = A()
print(hasattr(a, "__x"), hasattr(a, "_A__x"))

# 6
class P:
    def __init__(self):
        self._v = 1
    @property
    def v(self):
        return self._v
p = P()
try:
    p.v = 5
except AttributeError:
    print("read-only")
print(p.v)

# 7
class A:
    x = 1
class B(A):
    pass
B.x = 2
print(A.x, B.x)

# 8
class A:
    x = 1
class B(A):
    pass
A.x = 5
print(B.x)

# 9
print(isinstance(True, int), issubclass(bool, int))

# 10
class S(ABC):
    @abstractmethod
    def f(self):
        ...
class T(S):
    pass
try:
    T()
except TypeError:
    print("cannot instantiate")
class U(S):
    def f(self):
        return "ok"
print(U().f())

# 11
class A:
    def __str__(self):
        return "A-str"
class B(A):
    pass
print(B())

# 12
class Duck:
    def speak(self):
        return "Quack"
class Robot:
    def speak(self):
        return "Beep"
print([x.speak() for x in (Duck(), Robot())])

# 13
class A:
    def f(self, x):
        return "one"
    def f(self, x, y):
        return "two"
try:
    print(A().f(1))
except TypeError:
    print("TypeError")
print(A().f(1, 2))

# 14
class Base:
    def __init__(self):
        self.items = []
class Child(Base):
    def __init__(self):
        self.extra = 1
        super().__init__()
print(sorted(vars(Child())))