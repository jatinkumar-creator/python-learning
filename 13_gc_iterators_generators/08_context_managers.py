import time
from contextlib import contextmanager

# 1. The class-based way: __enter__ and __exit__
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"took {self.elapsed:.4f}s")
        return False                    # False: do not swallow exceptions

with Timer() as t:
    sum(range(1_000_000))
print(t.elapsed > 0)

# 2. The generator way: code before yield is __enter__, after is __exit__
@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield label                     # the value bound by "as"
    finally:
        print(f"{label} took {time.perf_counter() - start:.4f}s")

with timer("sum") as name:
    print("inside", name)
    sum(range(1_000_000))

# 3. Both versions still clean up when an error happens
try:
    with timer("failing"):
        raise ValueError("oops")
except ValueError as e:
    print("error propagated:", e)

# 4. A context manager that temporarily changes something
import os

@contextmanager
def working_directory(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

before = os.getcwd()
with working_directory(".."):
    print("inside:", os.getcwd() != before)
print("restored:", os.getcwd() == before)