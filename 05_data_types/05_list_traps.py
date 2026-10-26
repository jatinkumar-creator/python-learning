# Trap 1: the 2D grid
grid = [[0] * 3] * 3
grid[0][0] = 5
print("Wrong grid:", grid)

grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 5
print("Right grid:", grid)

# Trap 2: += vs a = a + [x]
a = [1, 2]
b = a
a += [3]
print(a, b)

a = [1, 2]
b = a
a = a + [3]
print(a, b)

# Trap 3: mutable default argument
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))                        # the same list is reused!

def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_fixed(1))
print(add_item_fixed(2))