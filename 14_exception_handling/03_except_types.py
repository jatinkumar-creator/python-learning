import os
from contextlib import suppress

# 1. Several handlers: the FIRST matching one runs
def attempt(label, func):
    try:
        print(f"{label:<20}->", func())
    except ValueError:
        print(f"{label:<20}-> ValueError handler")
    except (TypeError, KeyError) as e:
        print(f"{label:<20}-> TypeError or KeyError handler: {e!r}")
    except ArithmeticError as e:
        print(f"{label:<20}-> ArithmeticError handler ({type(e).__name__})")
    except Exception as e:
        print(f"{label:<20}-> catch-all handler ({type(e).__name__})")
    else:
        print(f"{label:<20}-> no error")

attempt("int('x')", lambda: int("x"))
attempt("'a' + 1", lambda: "a" + 1)
attempt("{}['k']", lambda: {}["k"])
attempt("1 / 0", lambda: 1 / 0)
attempt("2.0 ** 10000", lambda: 2.0 ** 10000)
attempt("[][0]", lambda: [][0])
attempt("open missing file", lambda: open("nope.txt"))
attempt("fine", lambda: "ok")

# 2. Order matters: a general handler first hides the specific one
try:
    int("x")
except Exception:
    print("general handler ran")
except ValueError:
    print("specific handler: never reached")        # Python does not warn you

# 3. Catching a parent class
for func in (lambda: {}["k"], lambda: [][5]):
    try:
        func()
    except LookupError as e:
        print(type(e).__name__, "was caught by LookupError")

try:
    open(".")                                      # a folder, not a file
except OSError as e:
    print(type(e).__name__, "caught by OSError, errno:", e.errno)

# 4. The exception object
try:
    int("abc")
except ValueError as e:
    print(e.args, str(e), repr(e), type(e).__name__)

print(str(KeyError("k")), "|", str(ValueError("a", "b")))   # a famous quirk: KeyError quotes its message

# 5. The "as" name is deleted when the except block ends
try:
    1 / 0
except ZeroDivisionError as err:
    saved = err                                    # copy it if you need it later
try:
    print(err)
except NameError as e:
    print("NameError:", e)
print(type(saved).__name__)

# 6. A bare "except:" catches EVERYTHING, even SystemExit and KeyboardInterrupt
try:
    raise SystemExit("leaving")
except:
    print("bare except even stopped SystemExit")

try:
    try:
        raise SystemExit(3)
    except Exception:
        print("not reached")
except SystemExit as e:
    print("except Exception let SystemExit through, code:", e.code)

# 7. Nested try blocks
try:
    try:
        int("x")
    except KeyError:
        print("inner handler: wrong type, skipped")
    finally:
        print("inner finally")
except ValueError:
    print("outer handler caught the ValueError")

# 8. Ignoring one specific error on purpose
with suppress(FileNotFoundError):
    os.remove("file_that_does_not_exist.tmp")
print("continued after suppress")

# 9. ExceptionGroup and except* (Python 3.11 and newer), for several errors at once
try:
    raise ExceptionGroup("several problems", [ValueError("v"), TypeError("t")])
except* ValueError as eg:
    print("ValueError part:", eg.exceptions)
except* TypeError as eg:
    print("TypeError part:", eg.exceptions)






    

#Why did the specific ValueError handler never run in example 2?
#Why is a bare except: risky? What does except Exception leave alone, and why is that good?
#Why does print(err) fail after the except block?

#Pattern	                                       #Use when
#except ValueError:                   #	You expect one specific problem
#except (A, B):	                       #Two problems get the same handling
#except Parent:	#                    #You want a whole family (LookupError, OSError)
#except Exception as e:	              #At a program boundary, to log and continue
#except:(bare)	                                     #Almost never
#except*	                       You handle ExceptionGroups, usually from concurrent code