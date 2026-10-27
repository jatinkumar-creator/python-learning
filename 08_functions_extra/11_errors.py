# def f(a=1, b):                     # SyntaxError: non-default argument follows default
#     pass

# def f(a, b):
#     return a + b
# f(a=1, a=2)                        # SyntaxError: keyword argument repeated
# f(a=1, 2)                          # SyntaxError: positional argument follows keyword
# f(1)                               # TypeError: missing a required argument
# f(1, 2, c=3)                       # TypeError: unexpected keyword argument

# print(reduce(lambda a, b: a + b, [1, 2]))   # NameError: reduce is not imported

# def gen():
#     yield 1
# g = gen()
# next(g)
# next(g)                            # StopIteration

# class Dog:
#     def bark(self):
#         return "woof"
# Dog.bark()                         # TypeError: missing the 'self' argument

# result = map(lambda x: x * 2, [1, 2, 3])
# print(result[0])                   # TypeError: 'map' object is not subscriptable

# print(sum(map(int, ["1", "x"])))   # ValueError inside map