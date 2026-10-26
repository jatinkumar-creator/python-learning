items = [("Notebook", 3, 45.5), ("Pen", 10, 8.25), ("Bag", 1, 1299)]

print(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Total':>12}")
print("-" * 39)
grand = 0
for name, qty, price in items:
    total = qty * price
    grand += total
    print(f"{name:<12}{qty:>5}{price:>10.2f}{total:>12,.2f}")
print("-" * 39)
print(f"{'Grand total':<27}{grand:>12,.2f}")