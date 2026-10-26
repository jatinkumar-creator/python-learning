# Reverse a number and check for palindrome
n = int(input("Number: "))
original, rev = n, 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)
print("Palindrome" if rev == original else "Not a palindrome")

# GCD using the Euclidean algorithm
a, b = map(int, input("Two numbers: ").split())
while b:
    a, b = b, a % b
print("GCD:", a)