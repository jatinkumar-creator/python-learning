# Iterating a string and a list
for ch in "Hi":
    print(ch)
for fruit in ["apple", "kiwi"]:
    print(fruit)

# range() variations. Predict each first.
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(1, 10, 2)))
print(list(range(5, 0, -1)))
print(list(range(5, 1)))

# enumerate and zip
names = ["Asha", "Ravi"]
ages = [28, 31]
for i, name in enumerate(names, start=1):
    print(i, name)
for name, age in zip(names, ages):
    print(name, age)

# dictionary iteration
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)

# The loop variable survives after the loop
for i in range(3):
    pass
print("i after loop:", i)

# for-else: else runs only if the loop did NOT break
for n in [3, 5, 7]:
    if n % 2 == 0:
        print("Found an even number")
        break
else:
    print("No even number found")