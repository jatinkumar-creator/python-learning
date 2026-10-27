class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self._history = []

    @property
    def balance(self):                      # read-only from outside
        return self._balance

    @property
    def history(self):                      # a copy, so callers can't edit the real list
        return tuple(self._history)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._history.append(("withdraw", amount))

class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def withdraw(self, amount):
        if self._balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Balance cannot go below {self.MIN_BALANCE}")
        super().withdraw(amount)

acc = BankAccount("Asha", 500)
acc.deposit(250)
acc.withdraw(100)
print(acc.balance, acc.history)

for action in (lambda: setattr(acc, "balance", 10**6),
               lambda: acc.history.append(("hack", 1)),
               lambda: acc.withdraw(10_000)):
    try:
        action()
    except (AttributeError, ValueError) as e:
        print(type(e).__name__ + ":", e)

sav = SavingsAccount("Ravi", 5000)
sav.withdraw(3000)
print(sav.balance)
try:
    sav.withdraw(1500)
except ValueError as e:
    print("ValueError:", e)

accounts = [acc, sav]                       # polymorphism: the same call on both
for a in accounts:
    try:
        a.withdraw(900)
        print(a.owner, "ok, balance", a.balance)
    except ValueError as e:
        print(a.owner, "->", e)