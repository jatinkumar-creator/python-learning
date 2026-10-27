class BankAccount:
    interest_rate = 0.04

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def add_interest(self):
        self.deposit(round(self.balance * self.interest_rate, 2))

    def statement(self):
        print(f"Statement for {self.owner}")
        for kind, amount in self.history:
            print(f"  {kind:<10}{amount:>10.2f}")
        print(f"  {'balance':<10}{self.balance:>10.2f}")

    def __str__(self):
        return f"{self.owner}: {self.balance:,.2f}"

acc = BankAccount("Asha", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.add_interest()
acc.statement()

for action in (lambda: acc.withdraw(10_000), lambda: acc.deposit(-5), lambda: BankAccount("X", -1)):
    try:
        action()
    except ValueError as e:
        print("ValueError:", e)