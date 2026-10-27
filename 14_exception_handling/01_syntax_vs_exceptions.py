import subprocess
import sys

# ---------- Part A: syntax errors are caught at compile time ----------
samples = {
    "missing colon":   "if True\n    print('x')",
    "bad indentation": "if True:\nprint('x')",
    "unclosed paren":  "print('hi'",
    "unclosed string": "print('hi)",
    "keyword as name": "class = 5",
    "bad assignment":  "5 = x",
    "return outside":  "return 5",
}
for label, code in samples.items():
    try:
        compile(code, "<demo>", "exec")
    except SyntaxError as e:
        print(f"{label:<16}{type(e).__name__}: {e.msg} (line {e.lineno})")

# ---------- Part B: what that means for a real program ----------
def run(code):
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    print("  stdout:", repr(r.stdout))
    print("  last stderr line:", r.stderr.strip().splitlines()[-1])

print("\nSyntax error: NOTHING runs, not even the first line")
run("print('first line')\nprint('oops'\n")

print("Runtime exception: lines before the error DO run")
run("print('first line')\n1 / 0\nprint('never reached')")

# ---------- Part C: common runtime exceptions and their parents ----------
def recurse():
    return recurse()

def failing_assert():
    assert False, "demo"

triggers = [
    lambda: 1 / 0,
    lambda: int("abc"),
    lambda: "5" + 5,
    lambda: undefined_name,
    lambda: [1][5],
    lambda: {}["k"],
    lambda: "x".nope,
    lambda: open("no_such_file.txt"),
    lambda: __import__("no_such_module"),
    lambda: next(iter([])),
    lambda: b"\xff".decode("utf-8"),
    lambda: float("x"),
    recurse,
    failing_assert,
]
print()
for trigger in triggers:
    try:
        trigger()
    except Exception as e:
        parents = " > ".join(c.__name__ for c in type(e).__mro__[1:-1])
        print(f"{type(e).__name__:<20}{parents:<38}{str(e)[:40]}")

# ---------- Part D: the hierarchy ----------
def show(cls, depth=0, max_depth=2):
    print("  " * depth + cls.__name__)
    if depth < max_depth:
        for sub in sorted(cls.__subclasses__(), key=lambda c: c.__name__):
            show(sub, depth + 1, max_depth)

print()
show(BaseException)




#Why did the first run() print an empty stdout, while the second printed first line?
#Which exceptions descend from BaseException but not from Exception? (Look at the tree, and note why you should rarely catch those.)
#Which parents do KeyError, FileNotFoundError, ModuleNotFoundError, and UnicodeDecodeError have?
#Is IndentationError a syntax error or an exception?





	#Syntax                          #error	                             #Exception
   #Found	                   #Before the program runs (compile time)	    #While it runs
  #Can try/except catch it?	   #No (except through compile()/eval())	         #Yes
  #Typical cause	                #Typo, missing colon, bad indentation	  #Bad data, missing file, logic bug
    #Example	                               #if x == 1                              #1 / 0