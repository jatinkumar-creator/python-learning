import cmath
import math

# int: unlimited size
print(type(42), 2 ** 200)
print(7 // 2, -7 // 2, 7 % 3, -7 % 3, divmod(17, 5))
print(bin(10), oct(10), hex(255), (255).bit_length())
print(pow(2, 10, 1000))                  # modular power
print(int(3.9), int(-3.9), round(2.5), round(3.5))

# float: binary approximation
f = 0.1 + 0.2
print(f, f == 0.3, math.isclose(f, 0.3))
print(float("inf"), float("-inf"))
nan = float("nan")
print(nan == nan, math.isnan(nan))       # NaN is never equal to itself
print((2.0).is_integer())

# exact decimals
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

# complex
z = 3 + 4j
print(z.real, z.imag, abs(z), z.conjugate())
print(cmath.sqrt(-1))

try:
    print(math.sqrt(-1))
except ValueError as e:
    print("ValueError:", e)

try:
    print(z > 2j)
except TypeError as e:
    print("TypeError:", e)