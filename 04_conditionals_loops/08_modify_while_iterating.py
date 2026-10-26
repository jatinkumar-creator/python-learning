# The bug: removing items while looping over the same list
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print("Buggy result:", nums)

# Fix 1: build a new list
nums = [2, 4, 6, 8, 9]
odds = [n for n in nums if n % 2 != 0]
print("Fixed:", odds)

# Fix 2: loop over a copy
nums = [2, 4, 6, 8, 9]
for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n)
print("Fixed with copy:", nums)