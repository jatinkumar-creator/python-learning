nums = [10, 20, 30]
nums.append(40)
nums.insert(1, 15)
nums.extend([50, 60])
print(nums)
nums.remove(15)
last = nums.pop()
print(last, nums)
nums.sort(reverse=True)
print(nums)

# append vs extend
a = [1, 2]
a.append([3, 4])
a.extend([5, 6])
print(a, len(a))

# slicing
lst = [10, 20, 30, 40, 50]
print(lst[1:4], lst[-2:], lst[::-1], lst[10:])

# comprehension
squares = [x * x for x in range(6) if x % 2 == 0]
print(squares)

print([1, 2, 3] + [4], [0] * 3, [1, 2] * 2)
print(3 in lst, 30 in lst)