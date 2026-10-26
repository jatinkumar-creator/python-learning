name, age, pi = "Asha", 28, 3.14159

# Four approaches
print(f"{name} is {age}")
print("{} is {}".format(name, age))
print("{1} {0}".format("a", "b"))
print("{n} is {a}".format(n=name, a=age))
print("%s is %d years old" % (name, age))

from string import Template
print(Template("Hello $name").substitute(name=name))

# f-string extras
print(f"{age + 1}", f"{name.upper()}", f"{age=}", f"{name!r}")
print(f"{{literal braces}}")

# Format specs: predict each first
print(f"{pi:.2f}")
print(f"{pi:.2}")
print(f"{age:>8}|{name:<8}|{name:^8}|")
print(f"{'hi':*^9}")
print(f"{42:05d}")
print(f"{1234567:,}")
print(f"{0.256:.1%}")
print(f"{12345.678:.2e}")
print(f"{255:b} {255:o} {255:x} {255:X} {255:#x}")
print(f"{5:+d}")
print(f"{'Python':.3}")

width, prec = 10, 3
print(f"{pi:{width}.{prec}f}|")

# Table-style output
rows = [("Asha", 28, 82.5), ("Ravi", 31, 91.25)]
print(f"{'Name':<10}{'Age':>5}{'Marks':>8}")
for n, a, m in rows:
    print(f"{n:<10}{a:>5}{m:>8.1f}")

# The % tuple trap
t = (1, 2)
try:
    print("Value: %s" % t)
except TypeError as e:
    print("TypeError:", e)
print("Value: %s" % (t,))