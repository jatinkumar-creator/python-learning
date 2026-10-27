from contextlib import contextmanager
from common import SCRATCH

p = SCRATCH / "with_demo.txt"

# The manual way: you must remember to close
f = open(p, "w", encoding="utf-8")
try:
    f.write("manual\n")
finally:
    f.close()
print("manual, closed:", f.closed)

# The with block closes the file for you
with open(p, "w", encoding="utf-8") as f:
    f.write("with block\n")
print("with, closed:", f.closed)

# Even when an error happens inside the block
try:
    with open(p, "w", encoding="utf-8") as f:
        f.write("before the error\n")
        raise RuntimeError("boom")
except RuntimeError as e:
    print("caught:", e, "| file closed:", f.closed)
print(repr(p.read_text(encoding="utf-8")))

# Two files in one with statement
src = SCRATCH / "src.txt"
dst = SCRATCH / "dst.txt"
src.write_text("line A\nline B\n", encoding="utf-8")
with open(src, encoding="utf-8") as fin, open(dst, "w", encoding="utf-8") as fout:
    for line in fin:
        fout.write(line.upper())
print(dst.read_text(encoding="utf-8"))

# Preview: your own context manager (you will understand it fully after OOP and generators)
@contextmanager
def announce(label):
    print("enter", label)
    try:
        yield label
    finally:
        print("exit ", label)

with announce("demo") as name:
    print("inside", name)

try:
    with announce("failing"):
        raise ValueError("oops")
except ValueError:
    print("the error still propagated, after cleanup")