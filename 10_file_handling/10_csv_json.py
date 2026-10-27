import csv
import json
from common import SCRATCH

# CSV
rows = [{"name": "Asha", "marks": 82, "city": "Delhi"},
        {"name": "Ravi", "marks": 91, "city": "Pune"},
        {"name": "Meera", "marks": 77, "city": "Delhi, NCR"}]     # a comma inside a value

csv_path = SCRATCH / "students.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:     # newline="" is required for csv
    w = csv.DictWriter(f, fieldnames=["name", "marks", "city"])
    w.writeheader()
    w.writerows(rows)
print(csv_path.read_text(encoding="utf-8"))

with open(csv_path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], int(row["marks"]) + 1, type(row["marks"]))   # values are strings

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header, list(reader))

# JSON
data = {"name": "Asha", "skills": ["python", "sql"], "active": True, "manager": None, "नाम": "आशा"}
json_path = SCRATCH / "profile.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(json_path.read_text(encoding="utf-8"))

with open(json_path, encoding="utf-8") as f:
    back = json.load(f)
print(back == data, back["manager"] is None)

# What JSON changes
print(json.loads(json.dumps({"t": (1, 2), 1: "x"})))             # tuple -> list, int key -> string

try:
    json.loads("{bad json}")
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e)

try:
    json.dumps({"s": {1, 2}})
except TypeError as e:
    print("TypeError:", e)