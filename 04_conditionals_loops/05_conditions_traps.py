x = 2

# Trap 1: this is always true. Why?
if x == 1 or 2:
    print("Trap 1: always prints")

# Fixed versions
if x == 1 or x == 2:
    print("Fixed with or")
if x in (1, 2):
    print("Fixed with in")

# Chained comparison
print(1 < x < 10)

# Short-circuit protects against division by zero
d = 0
if d != 0 and 10 / d > 2:
    print("Not reached")
else:
    print("Safe: no ZeroDivisionError")