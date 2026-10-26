age = int(input("Age: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")

# The same logic, flattened
if age >= 18 and has_id:
    print("Entry allowed (flat version)")