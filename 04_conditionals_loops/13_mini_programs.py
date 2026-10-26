# 1. Leap year
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 2. Factorial
n = int(input("n for factorial: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
print(fact)

# 3. First n Fibonacci numbers
n = int(input("How many Fibonacci numbers: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 4. Prime check using for-else
n = int(input("Number to check: "))
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# 5. FizzBuzz
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)