class Item:
    def __init__(self, name, price, qty=1):
        self.name, self.price, self.qty = name, price, qty

    def total(self):
        return self.price * self.qty

    def __repr__(self):
        return f"Item({self.name!r}, {self.price}, x{self.qty})"

class Cart:
    discount_rate = 0.10

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(i.total() for i in self.items)

    def total_after_discount(self):
        return self.total() * (1 - self.discount_rate)

    def __len__(self):
        return len(self.items)

    def __contains__(self, name):
        return any(i.name == name for i in self.items)

cart = Cart()
cart.add(Item("Pen", 8.5, 10))
cart.add(Item("Notebook", 45, 3))
print(len(cart), "Pen" in cart, "Bag" in cart)
print(cart.total(), cart.total_after_discount())
for item in cart.items:
    print(f"{item.name:<10}{item.qty:>3} x {item.price:>6.2f} = {item.total():>8.2f}")