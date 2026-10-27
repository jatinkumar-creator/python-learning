# from abc import ABC, abstractmethod
# class S(ABC):
#     @abstractmethod
#     def f(self):
#         ...
# S()                                   # TypeError: can't instantiate abstract class

# class A:
#     def __init__(self):
#         self.name = "a"
# class B(A):
#     def __init__(self):
#         pass
# print(B().name)                       # AttributeError: super().__init__() was never called

# class A:
#     def __init__(self):
#         self.__x = 1
# print(A().__x)                        # AttributeError: name mangling

# class P:
#     @property
#     def v(self):
#         return 1
# P().v = 2                             # AttributeError: no setter

# class X: pass
# class Y(X): pass
# class Z(X, Y): pass                   # TypeError: cannot create a consistent MRO

# class A:
#     def __init__(self, x):
#         self.x = x
# class B(A):
#     def __init__(self):
#         super().__init__()            # TypeError: missing the 'x' argument
# B()

# class B(Undefined): pass              # NameError

# super().__init__()                    # RuntimeError: super(): no arguments (outside a class)

# class A:
#     def f(self):
#         return 1
# class B(A):
#     def f(self, x):
#         return super().f() + x
# print([o.f() for o in (A(), B())])    # TypeError on B: the signature changed, polymorphism broke