# 1
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# 2
nums = [3, 1, 2]
print(nums.sort(), nums)

# 3
a = [1, 2]
a.append([3, 4])
a.extend([5, 6])
print(a, len(a))

# 4
lst = [10, 20, 30, 40, 50]
print(lst[1:4], lst[-2:], lst[::-1], lst[10:])

# 5
grid = [[0] * 2] * 2
grid[0][0] = 5
print(grid)

# 6
print([x * x for x in range(5) if x % 2 == 0])

# 7
print(["even" if x % 2 == 0 else "odd" for x in range(3)])

# 8
t = ([1, 2], 3)
t[0].append(9)
print(t)

# 9
print(type((5)), type((5,)), type(()))

# 10
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

# 11
print({1, 2, 3, 3, 2}, len({1, 2, 3, 3, 2}), type({}))

# 12
a, b = {1, 2, 3}, {3, 4}
print(sorted(a | b), a & b, sorted(a - b), sorted(a ^ b))

# 13
print(list(dict.fromkeys([3, 1, 3, 2, 1])))

# 14
d = {"a": 1, "b": 2}
print(d.get("c"), d.get("c", 0), "a" in d, 1 in d.values())

# 15
d = {"x": 1}
d.setdefault("y", 5)
d.setdefault("x", 9)
print(d)

# 16
print({"x": 1, "y": 2} | {"y": 20, "z": 30})

# 17
d = dict.fromkeys("ab", [])
d["a"].append(1)
print(d)

# 18
print({k: v for k, v in zip("abc", range(3))})

# 19
print(sorted({"b": 1, "a": 2}), sorted({"b": 1, "a": 2}.items(), key=lambda kv: kv[1]))

# 20
fs = frozenset([1, 2])
print(fs | {3}, type(fs | {3}))