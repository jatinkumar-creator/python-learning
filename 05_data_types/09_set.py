s = {1, 2, 3, 3, 2}
print(s, len(s), type({}), type(set()))

s.add(4)
s.discard(10)                             # no error
try:
    s.remove(10)
except KeyError as e:
    print("KeyError:", e)

a, b = {1, 2, 3}, {3, 4}
print(a | b, a & b, a - b, a ^ b)
print({1, 2} <= {1, 2, 3}, a.isdisjoint({9}))

# removing duplicates
items = [3, 1, 3, 2, 1]
print(list(set(items)))                   # order not guaranteed
print(list(dict.fromkeys(items)))         # order preserved

try:
    print(s[0])
except TypeError as e:
    print("TypeError:", e)

# frozenset
fs = frozenset([1, 2, 3, 2])
print(fs, fs | {4}, type(fs | {4}))
try:
    fs.add(5)
except AttributeError as e:
    print("AttributeError:", e)

routes = {frozenset({"Delhi", "Pune"}): 1450}
print(routes[frozenset({"Pune", "Delhi"})])