from common import SCRATCH

p = SCRATCH / "modes.txt"

def show(label):
    print(f"{label:<30}", repr(p.read_text(encoding="utf-8")))

with open(p, "w", encoding="utf-8") as f:
    f.write("line 1\n")
show("after w")

with open(p, "a", encoding="utf-8") as f:
    f.write("line 2\n")
show("after a (appended)")

with open(p, "w", encoding="utf-8") as f:
    f.write("only line\n")
show("after w again (truncated!)")

try:
    with open(p, "x", encoding="utf-8") as f:
        f.write("never written")
except FileExistsError as e:
    print("x on an existing file -> FileExistsError:", e)

try:
    with open(SCRATCH / "missing.txt", encoding="utf-8") as f:
        pass
except FileNotFoundError as e:
    print("r on a missing file -> FileNotFoundError:", e)

with open(p, "r+", encoding="utf-8") as f:
    print("r+ read:", repr(f.read()))
    f.write("added by r+\n")             # the position is at the end after read()
show("after r+")

with open(p, "a+", encoding="utf-8") as f:
    f.write("added by a+\n")
    f.seek(0)
    print("a+ read back:", repr(f.read()))

with open(p, "w+", encoding="utf-8") as f:
    f.write("fresh")
    f.seek(0)
    print("w+ read back:", repr(f.read()))

try:
    with open(p, "r", encoding="utf-8") as f:
        f.write("nope")
except Exception as e:
    print(type(e).__name__ + ":", e)

try:
    with open(p, "w", encoding="utf-8") as f:
        f.read()
except Exception as e:
    print(type(e).__name__ + ":", e)