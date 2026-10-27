class BankError(Exception):
    """Base class for banking problems."""

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f"balance {balance:.2f}, requested {amount:.2f}")
        self.balance, self.amount = balance, amount

class AccountFrozenError(BankError):
    pass

class Account:
    def __init__(self, owner, balance=0):
        self.owner, self.balance, self.frozen = owner, balance, False
        self.log = []

    def _check(self, amount):
        if self.frozen:
            raise AccountFrozenError(f"{self.owner}'s account is frozen")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountError(f"invalid amount: {amount!r}")

    def deposit(self, amount):
        self._check(amount)
        self.balance += amount
        self.log.append(("deposit", amount))

    def withdraw(self, amount):
        self._check(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        self.log.append(("withdraw", amount))

def transfer(source, target, amount):
    original = source.balance
    try:
        source.withdraw(amount)
        target.deposit(amount)
    except BankError:
        source.balance = original                 # roll back, then let the caller decide
        raise

a, b = Account("Asha", 500), Account("Ravi", 100)
b.frozen = False

steps = [
    ("deposit 200", lambda: a.deposit(200)),
    ("withdraw 50", lambda: a.withdraw(50)),
    ("withdraw -5", lambda: a.withdraw(-5)),
    ("withdraw 9999", lambda: a.withdraw(9999)),
    ("transfer 300", lambda: transfer(a, b, 300)),
    ("freeze Ravi, transfer 100", lambda: (setattr(b, "frozen", True), transfer(a, b, 100))),
]
for label, action in steps:
    try:
        action()
        print(f"{label:<28}OK    Asha={a.balance} Ravi={b.balance}")
    except InsufficientFundsError as e:
        print(f"{label:<28}FUNDS {e} (short by {e.amount - e.balance:.2f})")
    except BankError as e:
        print(f"{label:<28}{type(e).__name__}: {e}")