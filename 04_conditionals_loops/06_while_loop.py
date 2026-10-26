# Counting
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# Sum of digits
n = 472
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Digit sum:", total)

# while-else: else runs unless the loop ends with break
count = 0
while count < 3:
    count += 1
else:
    print("Loop finished normally")

# Input validation with while True
while True:
    s = input("Enter a positive number: ")
    if s.isdigit() and int(s) > 0:
        break
    print("Invalid, try again")
print("You entered", s)