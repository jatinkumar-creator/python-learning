inventory = {"pen": {"qty": 100, "price": 8.5},
             "notebook": {"qty": 40, "price": 45.0}}

def add_stock(name, qty, price=None):
    item = inventory.setdefault(name, {"qty": 0, "price": price or 0})
    item["qty"] += qty

def total_value():
    return sum(i["qty"] * i["price"] for i in inventory.values())

add_stock("pen", 20)
add_stock("bag", 5, 1299)
for name, i in inventory.items():
    print(f"{name:<10}{i['qty']:>5}{i['price']:>10.2f}")
print(f"Total value: {total_value():,.2f}")

low = [n for n, i in inventory.items() if i["qty"] < 10]
print("Low stock:", low)