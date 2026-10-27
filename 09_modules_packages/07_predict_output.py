import sys
import math

# 1
print("math" in sys.modules, sys.modules["math"] is math)

# 2
import math as m
print("math" in dir(), "m" in dir())

# 3
from math import sqrt
print("sqrt" in dir(), "pi" in dir())

# 4
print(__name__)

# 5
print(__import__("math").floor(2.7))

# 6
import os.path
print(type(os.path).__name__, os.path.basename("a/b/c.txt"), os.path.splitext("c.txt"))

# 7
from collections import Counter as C
print(C("aab"))

# 8
import json
print(json.dumps({"a": 1, "b": [1, 2]}), json.loads('{"x": [1, 2]}')["x"][1])

# 9
from datetime import date
print(date(2026, 10, 27).strftime("%d-%m-%Y"), date(2026, 10, 27).strftime("%A"))

# 10
from pathlib import Path
p = Path("a/b/c.txt")
print(p.name, p.suffix, p.stem)

# 11
import statistics
print(statistics.mean([1, 2, 3, 4]), statistics.median([1, 3, 2]))

# 12
print(sys.argv)

# 13
sqrt = 5
try:
    sqrt(4)
except TypeError:
    print("sqrt was overwritten")

# 14
import itertools
print(list(itertools.combinations([1, 2, 3], 2)))

# 15
print(sorted(set(dir(math)) & {"sqrt", "pi", "nope"}))