# 1
print(type(5), type(5.0), type(5j), type(True), type(None))

# 2
print(7 // 2, -7 // 2, 7 % -3, divmod(17, 5))

# 3
print(bool(""), bool(" "), bool([[]]), bool(0.0), bool("False"))

# 4
print(float("nan") == float("nan"))

# 5
print((2 + 3j) * (1 - 1j))

# 6
print(int(-3.7), round(-3.7), round(2.5), round(3.5))

# 7
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# 8
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)

# 9
nums = [3, 1, 2]
print(nums.sort(), nums)

# 10
d = {"a": 1, "b": 2}
print(d.get("c"), d.get("c", 0), "a" in d, 1 in d.values())

# 11
print({1: "a", 1.0: "b", True: "c"})

# 12
print({1, 2, 3} | {3, 4}, {1, 2, 3} & {3, 4}, {1, 2, 3} ^ {3, 4})

# 13
print(list(dict.fromkeys([3, 1, 3, 2, 1])))

# 14
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

# 15
t = ([1, 2], 3)
t[0].append(9)
print(t)