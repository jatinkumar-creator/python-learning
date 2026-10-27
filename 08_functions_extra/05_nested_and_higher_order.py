# Nested (inner) function
def outer():
    def inner():
        return "inner called"
    return inner()

print(outer())

# Function as argument
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda n: n * 2, 5))
print(apply_twice(str.upper, "hi"))

def apply_all(funcs, value):
    return [f(value) for f in funcs]

print(apply_all([str.upper, str.title, len], "hello world"))

# Function as return value
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5), make_multiplier(10)(4))

def choose(op):
    if op == "add":
        return lambda a, b: a + b
    return lambda a, b: a - b

print(choose("add")(5, 3), choose("sub")(5, 3))

# Functions stored in data structures
ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}
for sym, fn in ops.items():
    print(sym, fn(3, 4))

# Closure: the inner function remembers its environment
def make_counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step

c1, c2 = make_counter(), make_counter()
print(c1(), c1(), c1(), c2())
print(c1.__closure__[0].cell_contents)