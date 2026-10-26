students = {
    "Asha":  {"marks": [82, 90, 76], "city": "Delhi"},
    "Ravi":  {"marks": [91, 85, 88], "city": "Pune"},
    "Meera": {"marks": [77, 70, 65], "city": "Delhi"},
}

for name, info in students.items():
    avg = sum(info["marks"]) / len(info["marks"])
    print(f"{name:<8}{avg:>6.1f}  {info['city']}")

best = max(students, key=lambda n: sum(students[n]["marks"]))
print("Top student:", best)

cities = {info["city"] for info in students.values()}
print("Cities:", sorted(cities))