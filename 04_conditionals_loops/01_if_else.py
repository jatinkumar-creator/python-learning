age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Ternary expression
status = "Adult" if age >= 18 else "Minor"
print(status)

# Truthiness
items = []
if not items:
    print("The list is empty")

name = ""
if name:
    print("Has a name")
else:
    print("Empty string is falsy")