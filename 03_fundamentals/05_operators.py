# Arithmetic
print(7 + 2, 7 - 2, 7 * 2, 7 / 2, 7 // 2, 7 % 2, 7 ** 2)
print(-7 // 2, -7 % 3, 7 % -3)       # predict these first
print(2 ** 3 ** 2)                    # right-associative

# Comparison and chaining
x = 5
print(x == 5, x != 5, x > 3, 1 < x < 10)

# Assignment and walrus
x += 2
x **= 2
print(x)
data = [1, 2, 3]
if (n := len(data)) > 2:
    print("long list:", n)

# Logical operators return operands
print(0 or "hi", "" and 5, 3 and 5, None or 0, not 0)

# Bitwise
print(5 & 3, 5 | 3, 5 ^ 3, ~5, 1 << 3, 16 >> 2)

# Membership and identity
print("a" in "cat", 3 not in [1, 2])
a = [1]
b = [1]
c = a
print(a == b, a is b, a is c)
print(None is None)

# Precedence
print(2 + 3 * 4, (2 + 3) * 4, 7 % 3 ** 2)