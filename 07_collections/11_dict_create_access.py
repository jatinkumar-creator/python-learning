d1 = {"name": "Asha", "age": 28}
d2 = dict(name="Asha", age=28)
d3 = dict([("a", 1), ("b", 2)])
d4 = dict(zip(["x", "y"], [1, 2]))
d5 = dict.fromkeys(["a", "b"], 0)
empty = {}
print(d1, d2, d3, d4, d5, empty, sep="\n")
print(d1 == d2, len(d1), type(d1))

# Accessing
person = {"name": "Asha", "age": 28, "city": "Delhi"}
print(person["name"])
print(person.get("phone"), person.get("phone", "N/A"))
print("name" in person, "Asha" in person, "Asha" in person.values())

try:
    print(person["phone"])
except KeyError as err:
    print("KeyError:", err)

print(list(person), list(person.keys()), list(person.values()), list(person.items()))

# Views are live
keys = person.keys()
person["email"] = "a@x.com"
print(keys)

# Nested dictionaries
company = {"asha": {"role": "Dev", "skills": ["py", "sql"]},
           "ravi": {"role": "QA", "skills": ["selenium"]}}
print(company["asha"]["skills"][0])
print(company.get("meera", {}).get("role", "unknown"))