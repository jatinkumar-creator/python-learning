# 1. try/finally vs a with block
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"open  {name}")

    def close(self):
        print(f"close {self.name}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        print("  __exit__ saw:", exc_type.__name__ if exc_type else None)
        return False                        # False: let the exception continue

r = Resource("manual")
try:
    print("working")
    raise RuntimeError("crash")
except RuntimeError as e:
    print("caught:", e)
finally:
    r.close()

try:
    with Resource("with-block") as res:
        print("working")
        raise RuntimeError("crash")
except RuntimeError as e:
    print("caught after cleanup:", e)

# 2. __exit__ returning True swallows the exception
class Quiet(Resource):
    def __exit__(self, exc_type, exc, tb):
        super().__exit__(exc_type, exc, tb)
        return True

with Quiet("quiet"):
    raise RuntimeError("swallowed")
print("program continues")

# 3. An error during cleanup can replace the original one
class Fragile:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        raise OSError("cleanup failed")

try:
    with Fragile():
        raise ValueError("original problem")
except OSError as e:
    print("OSError:", e, "| context:", repr(e.__context__))

# 4. Retry loop with for/else
attempts = {"n": 0}

def flaky():
    attempts["n"] += 1
    if attempts["n"] < 3:
        raise ConnectionError(f"attempt {attempts['n']} failed")
    return "connected"

for attempt in range(1, 5):
    try:
        print(flaky())
        break
    except ConnectionError as e:
        print("  retrying after:", e)
else:
    print("gave up")