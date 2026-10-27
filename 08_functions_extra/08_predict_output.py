from functools import reduce

# 1
print(any([]), all([]))

# 2
print(any([0, "", None]), any([0, 1]), all([1, "a"]), all([1, 0]))

# 3
print(list(map(lambda x, y: x + y, [1, 2], [10, 20])))

# 4
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))

# 5
print(list(filter(None, [0, 1, "", 2, None])))

# 6
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

# 7
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])

# 8
print((lambda *a: sum(a))(1, 2, 3))

# 9
def f():
    return 1, 2
print(type(f()), f())

# 10
def d1(func):
    def w():
        return "<b>" + func() + "</b>"
    return w

def d2(func):
    def w():
        return "<i>" + func() + "</i>"
    return w

@d1
@d2
def hi():
    return "hi"
print(hi())

# 11
g = (x * x for x in range(3))
print(list(g), list(g))

# 12
def make():
    return lambda: "called"
print(make()())

# 13
def f(a, b=[], *args, **kw):
    b.append(a)
    return b
print(f(1), f(2))

# 14
print(sorted(["bb", "a", "cc", "d"], key=len))

# 15
def outer():
    n = 0
    def inner():
        nonlocal n
        n += 1
        return n
    return inner
c = outer()
c()
print(c())