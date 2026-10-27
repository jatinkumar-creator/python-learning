contacts = {}

while True:
    print("\n1. Add  2. Search  3. Delete  4. List  5. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        name = input("Name: ").strip().title()
        phone = input("Phone: ").strip()
        contacts[name] = phone
        print("Saved.")
    elif choice == "2":
        name = input("Name: ").strip().title()
        print(contacts.get(name, "Not found"))
    elif choice == "3":
        name = input("Name: ").strip().title()
        if contacts.pop(name, None) is None:
            print("Not found")
        else:
            print("Deleted.")
    elif choice == "4":
        for name, phone in sorted(contacts.items()):
            print(f"{name:<12}{phone}")
    elif choice == "5":
        break
    else:
        print("Invalid choice")