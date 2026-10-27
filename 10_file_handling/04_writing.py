from common import SCRATCH

p = SCRATCH / "writing.txt"

with open(p, "w", encoding="utf-8") as f:
    n = f.write("Hello\n")
    print("write returned:", n)         # the number of characters written
    f.writelines(["a", "b", "c"])       # writelines does NOT add newlines
    f.write("\n")
    f.writelines(f"{i}\n" for i in range(3))
    print("via print()", file=f)
    print(1, 2, 3, sep=",", file=f)
    try:
        f.write(42)
    except TypeError as e:
        print("TypeError:", e)
    f.flush()                           # push buffered data to disk now

print(repr(p.read_text(encoding="utf-8")))

# A formatted table written to a file
rows = [("Asha", 28, 82.5), ("Ravi", 31, 91.25)]
with open(p, "w", encoding="utf-8") as f:
    f.write(f"{'Name':<10}{'Age':>5}{'Marks':>8}\n")
    for name, age, marks in rows:
        f.write(f"{name:<10}{age:>5}{marks:>8.1f}\n")
print(p.read_text(encoding="utf-8"))

# Shortcuts for small files
p.write_text("replaced\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))