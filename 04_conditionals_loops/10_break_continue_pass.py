# break: leave the loop
for n in range(1, 10):
    if n == 5:
        break
    print(n, end=" ")
print()

# continue: skip this iteration
for n in range(1, 6):
    if n == 3:
        continue
    print(n, end=" ")
print()

# pass: placeholder
def todo():
    pass

class Empty:
    pass

for n in range(3):
    pass
print("pass did nothing")

# break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

# Exiting both loops: use a function and return
def find(grid, target):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == target:
                return r, c
    return None

print(find([[1, 2], [3, 4]], 3))