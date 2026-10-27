# ---------- Procedural: data and functions are separate ----------
account = {"owner": "Asha", "balance": 100}

def deposit(acc, amount):
    acc["balance"] += amount

def withdraw(acc, amount):
    if amount > acc["balance"]:
        return "Insufficient funds"
    acc["balance"] -= amount

deposit(account, 50)
print(withdraw(account, 500))
print(account)
account["balance"] = -999            # nothing stops anyone from breaking the data
print(account)

# ---------- Object-oriented: data and behaviour travel together ----------
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: {self.balance}"

a = Account("Asha", 100)
b = Account("Ravi", 500)             # many objects from one class, each with its own data
a.deposit(50)
print(a.withdraw(500))
print(a, "|", b)