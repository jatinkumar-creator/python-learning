import subprocess
import sys

def average(nums):
    assert len(nums) > 0, "nums must not be empty"
    return sum(nums) / len(nums)

print(average([1, 2, 3]))
try:
    average([])
except AssertionError as e:
    print("AssertionError:", e)

# assert is just shorthand for this
x = -1
try:
    if __debug__:
        if not (x >= 0):
            raise AssertionError("x must be non-negative")
except AssertionError as e:
    print("long form:", e)

print("__debug__ =", __debug__)

# Running Python with -O removes every assert
r = subprocess.run([sys.executable, "-O", "-c", "assert False, 'boom'\nprint('assert was skipped')"],
                   capture_output=True, text=True)
print(r.stdout.strip())

# Good uses: internal sanity checks, invariants, quick tests
def percent(part, whole):
    assert whole != 0, "caller must pass a non-zero whole"
    result = part / whole * 100
    assert 0 <= result <= 100 or part > whole
    return result

print(percent(1, 4))
assert sorted([3, 1, 2]) == [1, 2, 3], "sorted() is broken"

# Bad use: validating user input (disappears with -O). Use an exception instead.
def withdraw_bad(balance, amount):
    assert amount <= balance, "insufficient funds"       # do NOT do this
    return balance - amount

def withdraw_good(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount

# The tuple trap: this assert can never fail
# assert (1 == 2, "message")      # SyntaxWarning: assertion is always true (try it in 16_errors.py)