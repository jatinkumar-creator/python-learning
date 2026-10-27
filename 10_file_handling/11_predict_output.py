from common import SCRATCH

p = SCRATCH / "predict.txt"

# 1
with open(p, "w", encoding="utf-8") as f:
    f.write("first\n")
with open(p, "w", encoding="utf-8") as f:
    f.write("second\n")
print(repr(p.read_text(encoding="utf-8")))

# 2
with open(p, "a", encoding="utf-8") as f:
    f.write("third\n")
print(repr(p.read_text(encoding="utf-8")))

# 3
with open(p, encoding="utf-8") as f:
    a = f.read()
    b = f.read()
print(len(a) > 0, repr(b))

# 4
with open(p, encoding="utf-8") as f:
    print(type(f.readline()), type(f.readlines()))

# 5
with open(p, "w", encoding="utf-8") as f:
    f.writelines(["x", "y", "z"])
print(repr(p.read_text(encoding="utf-8")))

# 6
with open(p, "w", encoding="utf-8") as f:
    print(f.write("hello"))

# 7
with open(p, encoding="utf-8") as f:
    pass
print(f.closed)

# 8
p.write_text("abcdef", encoding="utf-8")
with open(p, "r+", encoding="utf-8") as f:
    f.write("XY")
print(p.read_text(encoding="utf-8"))

# 9
with open(p, encoding="utf-8") as f:
    f.seek(2)
    print(f.read(2), f.read(1))

# 10
try:
    with open(p, "x", encoding="utf-8") as f:
        pass
except FileExistsError:
    print("exists")

# 11
with open(p, "w", encoding="utf-8") as f:
    print("a", "b", sep="-", end="!", file=f)
print(repr(p.read_text(encoding="utf-8")))

# 12
p.write_text("one\ntwo\nthree\n", encoding="utf-8")
with open(p, encoding="utf-8") as f:
    print([len(line) for line in f])