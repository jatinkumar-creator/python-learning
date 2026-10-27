import sys
import math
import math as m
from math import sqrt, pi
from math import floor as fl
from math import *                    # imports everything public (avoid this in real code)

print(math.sqrt(16), m.sqrt(25), sqrt(36), fl(2.7))
print(pi, math.pi == m.pi)

print(type(math), math.__name__)
print(math.__file__ if hasattr(math, "__file__") else "built into the interpreter")
print("math" in sys.modules, sys.modules["math"] is math)

print(len(dir(math)), [n for n in dir(math) if n.startswith("c")][:6])
help(math.gcd)

# Importing a submodule
import os.path
print(type(os.path), os.path.join("a", "b"))

from collections import Counter as C
print(C("banana"))

# Names you bind are ordinary variables, so they can be overwritten
from math import sqrt
sqrt = 5
try:
    sqrt(4)
except TypeError as e:
    print("TypeError:", e)