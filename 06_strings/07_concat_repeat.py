print("Py" + "thon")
print("Age: " + str(28))
print("ab" * 3, "-" * 20)
print(repr("ab" * 0), repr("ab" * -2))

try:
    print("Age: " + 28)
except TypeError as e:
    print("TypeError:", e)

try:
    print("ab" * 2.0)
except TypeError as e:
    print("TypeError:", e)

print("5" + "3", "5" * 3, int("5") + int("3"))

# Comparison is lexicographic by code point
print("apple" < "banana", "Z" < "a", "10" < "9", "apple" < "Apple")

# join vs +=
words = ["Python", "is", "fun"]
result = ""
for w in words:
    result += w + " "
print(result.strip())
print(" ".join(words))