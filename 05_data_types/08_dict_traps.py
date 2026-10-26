# KeyError
d = {"a": 1}
try:
    print(d["b"])
except KeyError as e:
    print("KeyError:", e)

# Changing a dict while iterating
d = {1: "a", 2: "b", 3: "c"}
try:
    for k in d:
        if k == 2:
            del d[k]
except RuntimeError as e:
    print("RuntimeError:", e)

d = {k: v for k, v in {1: "a", 2: "b", 3: "c"}.items() if k != 2}
print(d)

# fromkeys with a mutable value
shared = dict.fromkeys("ab", [])
shared["a"].append(1)
print(shared)

separate = {k: [] for k in "ab"}
separate["a"].append(1)
print(separate)