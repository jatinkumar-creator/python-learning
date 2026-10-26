fruits = ["banana", "apple"]
fruits.append("cherry")
fruits.extend(["kiwi", "mango"])
fruits.insert(1, "fig")
print(fruits)

fruits.remove("apple")
print(fruits.pop(), fruits.pop(0), fruits)
print(fruits.index("cherry"), fruits.count("fig"))

# sort vs sorted, reverse vs reversed
nums = [3, 1, 2]
print(sorted(nums), nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums, list(reversed(nums)))

words = ["banana", "Apple", "cherry", "kiwi"]
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=len))

# Built-in functions on lists
print(len(nums), min(nums), max(nums), sum(nums))

# copy and clear
orig = [1, 2, 3]
dup = orig.copy()
orig.clear()
print(orig, dup)

# Methods that return None
print([3, 1, 2].sort())

# Errors
for action in [lambda: [1, 2].remove(9), lambda: [1, 2].index(9), lambda: [].pop()]:
    try:
        action()
    except (ValueError, IndexError) as err:
        print(type(err).__name__ + ":", err)