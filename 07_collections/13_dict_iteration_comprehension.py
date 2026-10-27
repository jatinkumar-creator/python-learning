from collections import Counter, defaultdict

scores = {"Asha": 82, "Ravi": 91, "Meera": 77}

for k in scores:
    print(k, end=" ")
print()
for v in scores.values():
    print(v, end=" ")
print()
for k, v in scores.items():
    print(f"{k:<6}{v:>4}")
for i, (k, v) in enumerate(scores.items(), start=1):
    print(i, k, v)

# Sorting
print(sorted(scores))
print(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))
print(dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True)))
print(max(scores, key=scores.get), min(scores, key=scores.get))

# Dictionary comprehension
print({n: n * n for n in range(5)})
print({k: v for k, v in scores.items() if v >= 80})
print({k: v + 5 for k, v in scores.items()})
print({v: k for k, v in scores.items()})                  # invert (values must be unique)
print({k: v for k, v in zip(["a", "b"], [1, 2])})
print({w: len(w) for w in ["apple", "kiwi"]})

# Counting
text = "the cat and the hat and the bat"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
print(freq)
print(Counter(text.split()).most_common(2))

# Grouping
groups = defaultdict(list)
for w in ["a", "bb", "cc", "d"]:
    groups[len(w)].append(w)
print(dict(groups))

# Modifying while iterating
d = {1: "a", 2: "b", 3: "c"}
try:
    for k in d:
        if k == 2:
            del d[k]
except RuntimeError as err:
    print("RuntimeError:", err)
d = {1: "a", 2: "b", 3: "c"}
for k in list(d):
    if k == 2:
        del d[k]
print(d)

# Key rules
try:
    bad = {[1, 2]: "a"}
except TypeError as err:
    print("TypeError:", err)
print({1: "a", 1.0: "b", True: "c"})