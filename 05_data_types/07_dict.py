person = {"name": "Asha", "age": 28}
print(person["name"], person.get("city"), person.get("city", "Unknown"))
person["city"] = "Delhi"
del person["age"]
print(person)

print("name" in person, "Asha" in person, "Asha" in person.values())

for k, v in person.items():
    print(k, v)

d = {"x": 1}
d.setdefault("y", 5)
d.setdefault("x", 9)                      # does not overwrite
print(d)

merged = {"a": 1, "b": 2} | {"b": 20, "c": 30}   # Python 3.9+
print(merged)

squares = {n: n * n for n in range(5)}
print(squares)

# key rules
try:
    bad = {[1, 2]: "a"}
except TypeError as e:
    print("TypeError:", e)

print({1: "a", 1.0: "b", True: "c"})      # predict this first

# sorting by value
scores = {"Asha": 82, "Ravi": 91, "Meera": 77}
print(max(scores, key=scores.get))
print(dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True)))