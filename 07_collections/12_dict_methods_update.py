d = {"a": 1, "b": 2}

# Updating
d["c"] = 3                         # add
d["a"] = 100                       # change
d.update({"b": 20, "d": 4})
d.update(e=5)
print(d)

d.setdefault("f", 6)
d.setdefault("a", 999)             # existing key is not overwritten
print(d)

# Removing
print(d.pop("f"), d.pop("zzz", "no such key"))
print(d.popitem())                 # removes the last inserted pair
del d["e"]
print(d)

# Merging
x = {"p": 1, "q": 2}
y = {"q": 20, "r": 30}
print(x | y, {**x, **y})
x |= y
print(x)

# Copy and clear
orig = {"k": [1, 2]}
shallow = orig.copy()
shallow["k"].append(3)
print(orig)
orig.clear()
print(orig, shallow)

# fromkeys trap
shared = dict.fromkeys("ab", [])
shared["a"].append(1)
print(shared)
separate = {k: [] for k in "ab"}
separate["a"].append(1)
print(separate)