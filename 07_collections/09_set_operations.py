a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b, a.union(b))
print(a & b, a.intersection(b))
print(a - b, a.difference(b))
print(a ^ b, a.symmetric_difference(b))
print({1, 2} <= a, {1, 2} < a, a >= {1}, a.issubset({1, 2, 3, 4, 5}))
print(a.isdisjoint({9}), a.isdisjoint(b))

# In-place versions
c = {1, 2, 3}
c |= {9}
c &= {1, 9, 10}
print(sorted(c))

# Practical uses
items = [3, 1, 3, 2, 1]
print(list(set(items)))                      # duplicates removed, order lost
print(list(dict.fromkeys(items)))            # duplicates removed, order kept
print(len(items) != len(set(items)))         # contains duplicates?
print(sorted(set(range(1, 7)) - {1, 2, 4, 6}))   # missing numbers

# Membership speed: list vs set
import timeit
big_list = list(range(100_000))
big_set = set(big_list)
print("list:", timeit.timeit("99_999 in big_list", globals=globals(), number=1000))
print("set :", timeit.timeit("99_999 in big_set", globals=globals(), number=1000))