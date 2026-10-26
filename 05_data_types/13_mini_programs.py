from collections import Counter

# 1. Word frequency
text = "the cat and the hat and the bat"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
print(freq)
print(Counter(text.split()))

# 2. Remove duplicates, keep order
nums = [3, 1, 3, 2, 1]
print(list(dict.fromkeys(nums)))

# 3. Second largest distinct number
nums = [10, 40, 20, 40, 30]
unique = sorted(set(nums))
print(unique[-2] if len(unique) >= 2 else "No second largest")

# 4. Two-sum (indexes of two numbers adding to a target)
nums, target = [2, 7, 11, 15], 9
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        print(seen[target - n], i)
        break
    seen[n] = i

# 5. Common elements of two lists
a, b = [1, 2, 3, 4], [3, 4, 5]
print(sorted(set(a) & set(b)))

# 6. Group words by length
from collections import defaultdict
words = ["a", "bb", "cc", "d"]
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))

# 7. Flatten a list of lists
nested = [[1, 2], [3], [4, 5]]
print([x for sub in nested for x in sub])

# 8. Transpose a matrix
m = [[1, 2, 3], [4, 5, 6]]
print([list(row) for row in zip(*m)])

# 9. Sort a list of dicts by a field
students = [{"name": "Asha", "marks": 82}, {"name": "Ravi", "marks": 91}]
print(sorted(students, key=lambda s: s["marks"], reverse=True)[0]["name"])

# 10. Does a list contain duplicates?
nums = [1, 2, 3, 2]
print(len(nums) != len(set(nums)))