while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Please enter a whole number.")

print("You entered", age)