nums = [10, 20, 30, 40, 50, 60]

# Predict each first
print(nums[1:4], nums[:3], nums[3:], nums[-2:])
print(nums[::2], nums[::-1], nums[10:], nums[-100:100])

copy1 = nums[:]                    # a shallow copy
copy1[0] = 999
print(nums, copy1)

# Slice assignment can change the list's length
nums[1:3] = [21, 22, 23]
print(nums)
nums[1:4] = []                     # deletes those items
print(nums)

# Extended slices need the same length
nums[::2] = [0, 0]
print(nums)
try:
    nums[::2] = [1, 2, 3]
except ValueError as err:
    print("ValueError:", err)

del nums[::2]
print(nums)