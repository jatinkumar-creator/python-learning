import collections
import datetime
import itertools
import json
import math
import os
import pathlib
import platform
import random
import re
import statistics
import time

# math and statistics
print(math.sqrt(16), math.floor(2.7), math.ceil(2.1), math.gcd(48, 18), math.factorial(5))
print(statistics.mean([1, 2, 3, 4]), statistics.median([1, 3, 2]), statistics.mode([1, 2, 2, 3]))

# random: values vary, but seeding makes them repeat on your machine
random.seed(42)
print(random.randint(1, 10), random.choice(["a", "b", "c"]), random.sample(range(10), 3))

# datetime
d = datetime.date(2026, 10, 27)
print(d, d.strftime("%d-%m-%Y"), d.strftime("%A"))
print(d + datetime.timedelta(days=30), (datetime.date(2026, 12, 25) - d).days)
print(datetime.date.today(), datetime.datetime.now().strftime("%H:%M"))

# collections and itertools
print(collections.Counter("banana").most_common(2))
dq = collections.deque([1, 2, 3])
dq.appendleft(0)
print(dq)
print(list(itertools.combinations("abc", 2)))
print(list(itertools.permutations([1, 2, 3], 2))[:3])
print(list(itertools.product("ab", [1, 2])))
print(list(itertools.chain([1, 2], [3])))

# json
data = {"name": "Asha", "skills": ["py", "sql"], "age": 28}
text = json.dumps(data, indent=2)
print(text)
print(json.loads(text) == data, type(json.loads("[1, 2]")))

# re
print(re.findall(r"\d+", "Order 12 shipped 3 items"))
print(re.sub(r"\s+", " ", "a    b   c"))

# os, pathlib, platform, time
print(os.getcwd())
print(pathlib.Path(__file__).name, pathlib.Path(__file__).suffix, pathlib.Path(__file__).stem)
print(pathlib.Path(__file__).resolve().parent)
print(platform.python_version(), platform.system())
start = time.perf_counter()
time.sleep(0.2)
print(round(time.perf_counter() - start, 1))