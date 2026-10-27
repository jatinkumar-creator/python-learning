import pickle

# 1. The simplest custom exception
class InvalidAgeError(Exception):
    pass

try:
    raise InvalidAgeError("age cannot be negative")
except InvalidAgeError as e:
    print(type(e).__name__, "-", e)

# 2. A hierarchy with one base class for the whole application
class AppError(Exception):
    """Base class for every error raised by this application."""

class ValidationError(AppError):
    def __init__(self, field, message):
        super().__init__(f"{field}: {message}")
        self.field = field
        self.message = message

class InsufficientFundsError(AppError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(f"balance {balance} is {self.shortfall} short for {amount}")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("amount", "must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

acct = Account(100)
for amount in (30, -5, 500):
    try:
        acct.withdraw(amount)
        print("withdrew", amount, "balance", acct.balance)
    except ValidationError as e:
        print("invalid input in field", e.field, "->", e.message)
    except InsufficientFundsError as e:
        print("need", e.shortfall, "more:", e)

# 3. Catch the whole family with the base class
try:
    acct.withdraw(10_000)
except AppError as e:
    print("AppError family caught:", type(e).__name__)

print(issubclass(InsufficientFundsError, AppError), issubclass(AppError, Exception))
print([c.__name__ for c in InsufficientFundsError.__mro__])

# 4. Wrapping a low-level error in a meaningful one
class ConfigError(AppError):
    pass

def read_port(text):
    try:
        port = int(text)
    except ValueError as e:
        raise ConfigError(f"port must be a number, got {text!r}") from e
    if not 1 <= port <= 65535:
        raise ConfigError(f"port out of range: {port}")
    return port

for text in ("8080", "http", "99999"):
    try:
        print("port", read_port(text))
    except ConfigError as e:
        print("ConfigError:", e, "| cause:", type(e.__cause__).__name__)

# 5. A subtle trap: a custom __init__ can break pickling and copying
try:
    pickle.loads(pickle.dumps(ValidationError("age", "negative")))
except TypeError as e:
    print("TypeError (pickle):", e)

class SafeValidationError(AppError):
    def __init__(self, field, message):
        super().__init__(field, message)            # args == (field, message), so Python can rebuild it
        self.field = field
        self.message = message

    def __str__(self):
        return f"{self.field}: {self.message}"

copy = pickle.loads(pickle.dumps(SafeValidationError("age", "negative")))
print(copy, "|", copy.field)




#Why inherit from Exception and not BaseException?
#Why does every application deserve a base exception such as AppError?
#Why name exceptions SomethingError, and what extra data (attributes) makes an exception more useful than a plain message?
#Why did the pickle round-trip fail for ValidationError, and how did SafeValidationError fix it? 