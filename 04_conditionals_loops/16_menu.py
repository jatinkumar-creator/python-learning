while True:
    print("\n1. Add  2. Subtract  3. Exit")
    choice = input("Choice: ")
    if choice == "3":
        print("Bye")
        break
    if choice not in ("1", "2"):
        print("Invalid choice")
        continue
    a, b = map(int, input("Two numbers: ").split())
    print(a + b if choice == "1" else a - b)