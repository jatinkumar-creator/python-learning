import copy

# Immutable: a new object on change
x = "abc"
print(id(x))
x += "d"
print(id(x))

# Mutable: the same object changes
y = [1]
print(id(y))
y.append(2)
print(id(y))

# Alias vs copy
a = [[1, 2], [3, 4]]
alias = a
shallow = a.copy()
deep = copy.deepcopy(a)

a[0].append(99)
print("alias  :", alias)
print("shallow:", shallow)
print("deep   :", deep)

# isinstance vs type
print(isinstance(True, int), type(True) == int)

# Memory: list vs tuple
import sys
print(sys.getsizeof([1, 2, 3]), sys.getsizeof((1, 2, 3)))