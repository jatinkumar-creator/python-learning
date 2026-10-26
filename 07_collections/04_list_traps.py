import copy

# Alias vs copies
a = [[1, 2], [3, 4]]
alias = a
shallow = a.copy()
deep = copy.deepcopy(a)
a[0].append(99)
print("alias  :", alias)
print("shallow:", shallow)
print("deep   :", deep)

# += vs a = a + [x]
a = [1, 2]
b = a
a += [3]
print(a, b)
a = [1, 2]
b = a
a = a + [3]
print(a, b)

# Modifying a list while iterating
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print("Buggy:", nums)
print("Fixed:", [n for n in [2, 4, 6, 8, 9] if n % 2 != 0])

# The sort() bug
data = [3, 1, 2]
data = data.sort()
print(data)