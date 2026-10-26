print(42, 0b1010, 0o17, 0xFF, 1_000_000)   # int literals
print(2 ** 200)                              # unlimited size
print(3.14, 2.5e3, 1e-4)                     # float literals
print(3 + 4j, (3 + 4j).real, (3 + 4j).imag)  # complex
print('hi', "hi", '''multi
line''', r"raw\n", f"{1 + 1}", b"bytes")     # strings
print(True, False, None)                     # bool and None
print([1, 2], (1, 2), {"a": 1}, {1, 2})      # collections

print(0.1 + 0.2)                             # float surprise
print(0.1 + 0.2 == 0.3)

import math
print(math.isclose(0.1 + 0.2, 0.3))

from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

print(True + True)                           # bool is a subclass of int