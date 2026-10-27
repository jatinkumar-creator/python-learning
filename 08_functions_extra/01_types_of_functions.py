# The four classic types, by arguments and return value
def say_hello():                 # no arguments, no return value
    print("Hello")

def greet(name):                 # arguments, no return value
    print(f"Hello, {name}")

def get_pi():                    # no arguments, returns a value
    return 3.14159

def add(a, b):                   # arguments and a return value
    return a + b

say_hello()
greet("Asha")
print(get_pi())
print(add(2, 3))
x = say_hello()
print(x)                         # None: a function without return gives None

# Built-in vs user-defined
print(len, type(len))
print(add, type(add))
print(callable(len), callable(add), callable(5))

# Pure vs impure functions
def pure_add(a, b):
    return a + b

total = 0
def impure_add(n):
    global total
    total += n
    return total

print(pure_add(2, 3), pure_add(2, 3))
print(impure_add(5), impure_add(5))     # same input, different output

# Generator function: yield instead of return
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))
gen = countdown(3)
print(next(gen), next(gen), next(gen))
try:
    next(gen)
except StopIteration:
    print("StopIteration: the generator is exhausted")