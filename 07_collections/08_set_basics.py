s = {3, 1, 2, 3, 2}
print(s, len(s), type({}), type(set()))
print(set("hello"), set([1, 1, 2]), set(range(3)))

# Iteration (order is not guaranteed, so sort it for stable output)
for x in sorted(s):
    print(x, end=" ")
print()
print(2 in s, 9 not in s)

# Adding and removing
s.add(4)
s.update([5, 6], {7})
s.discard(100)                     # no error
try:
    s.remove(100)
except KeyError as err:
    print("KeyError:", err)
print(sorted(s), s.pop() in range(1, 8))
s.clear()
print(s)

# Elements must be hashable, and there is no indexing
try:
    bad = {[1, 2], 3}
except TypeError as err:
    print("TypeError:", err)
try:
    print({1, 2}[0])
except TypeError as err:
    print("TypeError:", err)

# Comprehension
print({x % 3 for x in range(10)})