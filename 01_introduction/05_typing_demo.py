x = 10
print(type(x))
x = "now a string"          # dynamic typing: same name, new type
print(type(x))

try:
    print("5" + 5)          # strong typing: no silent conversion
except TypeError as e:
    print("TypeError:", e)

print("5" * 3)              # repetition, not arithmetic
print(int("5") + 5)         # explicit conversion works