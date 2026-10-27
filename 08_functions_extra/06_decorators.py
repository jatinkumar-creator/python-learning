import time
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b=0):
    """Add two numbers."""
    return a + b

add(2, 3)
add(5, b=1)
print(add.__name__, add.__doc__)

# Same thing written without @ syntax
def multiply(a, b):
    return a * b
multiply = log_calls(multiply)
multiply(3, 4)

# A decorator with its own arguments needs one more level
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()

# Stacking decorators: applied from the bottom up
def bold(f):
    @wraps(f)
    def w():
        return "<b>" + f() + "</b>"
    return w

def italic(f):
    @wraps(f)
    def w():
        return "<i>" + f() + "</i>"
    return w

@bold
@italic
def text():
    return "hi"

print(text())

# A practical one: a timer
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(2_000_000))