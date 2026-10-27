# 1
def f():
    try:
        return "a"
    finally:
        print("b")
print(f())

# 2
def f():
    try:
        1 / 0
    except ZeroDivisionError:
        return "except"
    finally:
        print("finally")
print(f())

# 3
try:
    print("try")
except ValueError:
    print("except")
else:
    print("else")
finally:
    print("finally")

# 4
try:
    int("x")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError")

# 5
try:
    [][0]
except (KeyError, IndexError) as e:
    print(type(e).__name__)

# 6
e = "before"
try:
    1 / 0
except ZeroDivisionError as e:
    pass
try:
    print(e)
except NameError:
    print("e is gone")

# 7
for i in range(3):
    try:
        if i == 1:
            continue
        print("body", i)
    finally:
        print("finally", i)

# 8
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("bad") from e
except ValueError as e:
    print(type(e.__cause__).__name__)

# 9
class MyErr(Exception):
    pass
try:
    raise MyErr("boom")
except Exception as e:
    print(type(e).__name__, e.args, str(e))

# 10
print(issubclass(KeyError, LookupError), issubclass(FileNotFoundError, OSError),
      issubclass(KeyboardInterrupt, Exception))

# 11
def f():
    for i in range(3):
        try:
            return i
        finally:
            print("cleanup", i)
print(f())

# 12
try:
    assert 1 == 2, "math is broken"
except AssertionError as e:
    print(e)

# 13
x = 0
try:
    x = 1
    raise ValueError
except ValueError:
    x += 10
finally:
    x += 100
print(x)

# 14
try:
    try:
        raise KeyError("k")
    except ValueError:
        print("inner")
except KeyError as e:
    print("outer", e)

# 15
print(str(ValueError("a", "b")), repr(ValueError("a")))

# 16
def g():
    try:
        raise ValueError("lost")
    finally:
        return "swallowed"
print(g())