from collections import Counter

# 1. Frequency of each element, most common first
nums = [1, 3, 2, 3, 1, 3]
print(Counter(nums).most_common())

# 2. Second largest distinct number
data = [10, 40, 20, 40, 30]
unique = sorted(set(data))
print(unique[-2] if len(unique) >= 2 else None)

# 3. Rotate a list right by k
items, k = [1, 2, 3, 4, 5], 2
k %= len(items)
print(items[-k:] + items[:-k])

# 4. Flatten one level
nested = [[1, 2], [3], [4, 5]]
print([x for sub in nested for x in sub])

# 5. Matrix addition
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print([[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(m1, m2)])

# 6. Matrix multiplication
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print([[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A])

# 7. Common, only-in-first, and all elements
a, b = [1, 2, 3, 4], [3, 4, 5]
print(sorted(set(a) & set(b)), sorted(set(a) - set(b)), sorted(set(a) | set(b)))

# 8. Two-sum indexes
arr, target = [2, 7, 11, 15], 9
seen = {}
for i, n in enumerate(arr):
    if target - n in seen:
        print(seen[target - n], i)
        break
    seen[n] = i

# 9. Group words by first letter
groups = {}
for w in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    groups.setdefault(w[0], []).append(w)
print(groups)

# 10. Student report from nested data
students = {"Asha": {"marks": [82, 90, 76], "city": "Delhi"},
            "Ravi": {"marks": [91, 85, 88], "city": "Pune"}}
for name, info in students.items():
    print(f"{name:<8}{sum(info['marks']) / len(info['marks']):>6.1f}  {info['city']}")

# 11. Anagram groups
words = ["listen", "silent", "enlist", "google", "gogole"]
groups = {}
for w in words:
    groups.setdefault("".join(sorted(w)), []).append(w)
print(list(groups.values()))