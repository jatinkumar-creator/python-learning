fs = frozenset([1, 2, 3, 2])
print(fs, len(fs), 2 in fs)

for x in sorted(fs):
    print(x, end=" ")
print()

print(fs | {4}, type(fs | {4}))
print(fs & {2, 3, 9})

for method in ("add", "remove", "discard", "pop", "update", "clear"):
    print(method, hasattr(fs, method))

# Hashable, so it can be a dict key or set element
routes = {frozenset({"Delhi", "Pune"}): 1450}
print(routes[frozenset({"Pune", "Delhi"})])
set_of_sets = {frozenset({1, 2}), frozenset({2, 1}), frozenset({3})}
print(len(set_of_sets))

print(frozenset(), hash(fs) == hash(frozenset([3, 2, 1])))