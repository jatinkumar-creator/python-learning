def min_max(nums):
    return min(nums), max(nums)          # several values become one tuple

result = min_max([4, 9, 1, 7])
print(result, type(result))
lo, hi = min_max([4, 9, 1, 7])
print(lo, hi)

def divide(a, b):
    if b == 0:
        return None                      # early return
    return a / b

print(divide(10, 2), divide(1, 0))

def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n                     # return exits the whole function
    return None

print(first_even([3, 5, 8, 10]), first_even([3, 5]))

def stats(nums):
    return {"min": min(nums), "max": max(nums), "avg": sum(nums) / len(nums)}

print(stats([1, 2, 3, 4]))

def no_value():
    return

print(no_value())