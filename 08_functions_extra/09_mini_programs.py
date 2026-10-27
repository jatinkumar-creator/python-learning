from functools import reduce, wraps

# 1. Password validator using all() and any()
def validate(pwd):
    rules = [
        lambda p: len(p) >= 8,
        lambda p: any(c.isupper() for c in p),
        lambda p: any(c.islower() for c in p),
        lambda p: any(c.isdigit() for c in p),
        lambda p: any(not c.isalnum() for c in p),
    ]
    return all(rule(pwd) for rule in rules)

print(validate("abc"), validate("P@ssw0rd!"))

# 2. Function composition
def compose(*funcs):
    return reduce(lambda f, g: lambda x: g(f(x)), funcs)

clean = compose(str.strip, str.lower, lambda s: s.replace(" ", "_"))
print(clean("  Hello World  "))

# 3. Memoizing decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))

# 4. Employee data with map / filter / reduce
employees = [
    {"name": "Asha",  "dept": "IT",    "salary": 60000},
    {"name": "Ravi",  "dept": "HR",    "salary": 45000},
    {"name": "Meera", "dept": "IT",    "salary": 75000},
]
it_staff = list(filter(lambda e: e["dept"] == "IT", employees))
print(list(map(lambda e: e["name"], it_staff)))
print(reduce(lambda acc, e: acc + e["salary"], employees, 0))
print(max(employees, key=lambda e: e["salary"])["name"])
print(sorted(employees, key=lambda e: e["salary"], reverse=True)[0]["name"])

# 5. Bank account built from a closure
def make_account(balance=0):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    def get_balance():
        return balance
    return deposit, withdraw, get_balance

deposit, withdraw, get_balance = make_account(100)
print(deposit(50), withdraw(30), withdraw(500), get_balance())

# 6. Input validation decorator
def positive_only(func):
    @wraps(func)
    def wrapper(n):
        if n <= 0:
            raise ValueError("n must be positive")
        return func(n)
    return wrapper

@positive_only
def square_root(n):
    return n ** 0.5

print(square_root(16))
try:
    square_root(-4)
except ValueError as e:
    print("ValueError:", e)