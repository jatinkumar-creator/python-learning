#try, except, else, finally
# 1. Which blocks run in which situation?
def flow(x):
    print(f"flow({x!r})")
    try:
        print("  try: start")
        value = 10 / x
        print("  try: end")
    except ZeroDivisionError:
        print("  except")
    else:
        print("  else, value =", value)
    finally:
        print("  finally")

for x in (2, 0):
    flow(x)

try:
    flow("a")
except TypeError as e:
    print("TypeError escaped after finally ran:", e)

# 2. A function that uses all four
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  cannot divide by zero")
        return None
    else:
        print("  no error, result is", result)
        return result
    finally:
        print("  finally always runs")

print(divide(10, 2))
print(divide(1, 0))

# 3. An error inside else is NOT handled by the except above it
try:
    try:
        x = 1
    except ValueError:
        print("never printed")
    else:
        int("abc")
except ValueError as e:
    print("outer handler caught it:", e)

# 4. finally runs even when you return, break, or continue
def f():
    try:
        return "from try"
    finally:
        print("cleanup runs BEFORE the function actually returns")

print(f())

for i in range(3):
    try:
        if i == 1:
            continue
        print("body", i)
    finally:
        print("finally", i)

# 5. A return inside finally overrides everything, even an exception. Avoid it.
def swallow():
    try:
        raise ValueError("lost")
    finally:
        return "the exception was swallowed"     # Python 3.14 may show a SyntaxWarning here

print(swallow())

# 6. EAFP vs LBYL
d = {"a": 1}

if "b" in d:                                     # Look Before You Leap
    v = d["b"]
else:
    v = 0

try:                                             # Easier to Ask Forgiveness than Permission
    v = d["b"]
except KeyError:
    v = 0

v = d.get("b", 0)                                # for dicts, a method can say it best
print(v)




#In which order do try, except, else, and finally run when there is no error? When there is an error that is caught? When it is not caught?
#Why put code in else instead of the end of try?
#Why is return inside finally dangerous?
#Why is check, then open the file (LBYL) less safe than try to open the file (EAFP)? 
#(Hint: the file can change between the check and the use.)