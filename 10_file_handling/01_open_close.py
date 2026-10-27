from common import SCRATCH

path = SCRATCH / "hello.txt"

f = open(path, "w", encoding="utf-8")
print(type(f))
print(f.name, f.mode, f.encoding, f.closed)
print(f.readable(), f.writable(), f.seekable())
f.write("Hello, file!\n")
f.close()
print("closed:", f.closed)

try:
    f.write("more")
except ValueError as e:
    print("ValueError:", e)

f = open(path, encoding="utf-8")        # the default mode is "r"
print(repr(f.read()))
f.close()