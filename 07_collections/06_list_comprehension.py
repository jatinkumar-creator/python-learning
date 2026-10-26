import sys

squares = [x * x for x in range(6)]
evens = [x for x in range(10) if x % 2 == 0]
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]   # if-else goes BEFORE for
pairs = [(x, y) for x in range(3) for y in range(2)]
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
words = ["apple", "kiwi", "banana"]
long_upper = [w.upper() for w in words if len(w) > 4]

print(squares, evens, labels, pairs, table, long_upper, sep="\n")

# Equivalent loop
result = []
for x in range(6):
    result.append(x * x)
print(result == squares)

# map/filter versions
print(list(map(lambda x: x * x, range(6))))
print(list(filter(lambda x: x % 2 == 0, range(10))))

# Generator expression: lazy, uses little memory
big_list = [x for x in range(1_000_000)]
big_gen = (x for x in range(1_000_000))
print(sys.getsizeof(big_list), sys.getsizeof(big_gen))
print(sum(x * x for x in range(1000)))

# Variables inside a comprehension do not leak
[y for y in range(3)]
try:
    print(y)
except NameError as err:
    print("NameError:", err)