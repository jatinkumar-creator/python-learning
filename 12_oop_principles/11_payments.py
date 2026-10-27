#(abstraction and the template method)
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def fee(self, amount):
        ...

    @abstractmethod
    def charge(self, amount):
        ...

    def checkout(self, amount):             # template method: the steps are fixed, the details vary
        if amount <= 0:
            raise ValueError("Amount must be positive")
        total = amount + self.fee(amount)
        self.charge(total)
        return total

class CreditCard(PaymentMethod):
    def fee(self, amount):
        return round(amount * 0.02, 2)
    def charge(self, amount):
        print(f"  Charging card {amount:.2f}")

class UPI(PaymentMethod):
    def fee(self, amount):
        return 0
    def charge(self, amount):
        print(f"  UPI payment {amount:.2f}")

class Wallet(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance
    def fee(self, amount):
        return 1
    def charge(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient wallet balance")
        self.balance -= amount
        print(f"  Wallet paid {amount:.2f}, left {self.balance:.2f}")

wallet = Wallet(500)
attempts = [(CreditCard(), 1000), (UPI(), 1000), (wallet, 300), (wallet, 400), (UPI(), -5)]
for method, amount in attempts:
    print(type(method).__name__, amount)
    try:
        print("  total:", method.checkout(amount))
    except ValueError as e:
        print("  ValueError:", e)