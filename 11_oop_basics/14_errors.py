# class A:
#     def m():                          # forgot self
#         pass
# A().m()                               # TypeError: takes 0 positional arguments but 1 was given

# class A:
#     def __init__(self, x):
#         self.x = x
# A()                                   # TypeError: missing 1 required positional argument: 'x'

# class A:
#     def __init__(self):
#         self.v = 1
#     def show(self):
#         print(v)                      # forgot self.
# A().show()                            # NameError: name 'v' is not defined

# class A:
#     pass
# A().nothing                           # AttributeError

# class A:
#     def __init__(self):
#         return 5                      # __init__ must return None
# A()                                   # TypeError

# class A:
#     def m(self):
#         pass
# A.m()                                 # TypeError: missing the 'self' argument

# class V:
#     def __init__(self, x):
#         self.x = x
# print(3 * V(1))                       # TypeError: unsupported operand (no __rmul__)

# class A:
#     pass
# a = A
# a.x = 1
# print(A().x)                          # AttributeError? Think about why: "a = A" has no parentheses