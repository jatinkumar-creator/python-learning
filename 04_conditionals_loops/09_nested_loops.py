# Multiplication grid
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# Right triangle
for i in range(1, 5):
    print("*" * i)

# Number triangle
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pyramid
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))