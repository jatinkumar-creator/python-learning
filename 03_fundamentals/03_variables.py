x = 10
print(type(x), id(x))
x = "hello"                    # dynamic typing: same name, new type
print(type(x), id(x))

a = b = c = 0                  # chained assignment
x, y, z = 1, 2, 3              # multiple assignment
first, *rest = [1, 2, 3, 4]    # extended unpacking
print(a, b, c, x, y, z, first, rest)

p, q = 5, 9
p, q = q, p                    # swap without a temp variable
print(p, q)

try:
    print("5" + 5)             # strong typing
except TypeError as e:
    print("TypeError:", e)

PI = 3.14159                   # constant by convention only
PI = 3                         # Python won't stop you
print(PI)