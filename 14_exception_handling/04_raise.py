import sys
import traceback

# 1. Raising your own errors for bad input
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if not 0 <= age <= 150:
        raise ValueError(f"age out of range: {age}")
    return age

for value in (30, -5, "x", 200):
    try:
        print("age set to", set_age(value))
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")

# 2. Raising a class vs an instance
try:
    raise ValueError                 # Python creates the instance for you
except ValueError as e:
    print(repr(e), e.args)

try:
    raise ValueError("with a message", 42)
except ValueError as e:
    print(repr(e), e.args)

# 3. Re-raising with a bare "raise" keeps the original traceback
def risky():
    try:
        1 / 0
    except ZeroDivisionError:
        print("logging the error, then re-raising")
        raise

try:
    risky()
except ZeroDivisionError as e:
    print("caller received:", e)

# 4. A bare raise outside an except block
try:
    raise
except RuntimeError as e:
    print("RuntimeError:", e)

# 5. Chaining: "raise ... from ..." records the cause
def load_number(text):
    try:
        return int(text)
    except ValueError as e:
        raise RuntimeError(f"bad config value {text!r}") from e

try:
    load_number("x")
except RuntimeError as e:
    print(e, "| cause:", repr(e.__cause__))
    traceback.print_exc(file=sys.stdout)     # note "direct cause" in the output

# 6. Raising inside an except block chains automatically (__context__)
try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise KeyError("something else")
except KeyError as e:
    print("context:", type(e.__context__).__name__, "| cause:", e.__cause__)

# 7. "from None" hides the original error from the traceback
def hide(text):
    try:
        return int(text)
    except ValueError:
        raise ValueError("please enter digits only") from None

try:
    hide("x")
except ValueError as e:
    print(e, "| suppressed context:", e.__suppress_context__)

# 8. Adding notes (Python 3.11 and newer)
try:
    try:
        int("x")
    except ValueError as e:
        e.add_note("while reading row 7")
        raise
except ValueError as e:
    print(e.__notes__)




    #What is the difference between raise, raise e, and raise NewError() from e?
    #When does a bare raise fail?
    #Why choose from None for a user-facing message, and why keep from e for debugging?