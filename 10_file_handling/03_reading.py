from common import SCRATCH

p = SCRATCH / "fruits.txt"
p.write_text("apple\nbanana\ncherry\ndate\n", encoding="utf-8")

with open(p, encoding="utf-8") as f:
    print(repr(f.read()))               # the whole file as one string
    print(repr(f.read()))               # empty: the pointer is already at the end

with open(p, encoding="utf-8") as f:
    print(repr(f.read(5)))              # the first 5 characters
    print(repr(f.readline()))           # the rest of that line
    print(repr(f.readline()))           # the next line
    print(type(f.tell()))               # a position (an opaque number in text mode)

with open(p, encoding="utf-8") as f:
    print(f.readlines())                # a list of lines, newlines included

with open(p, encoding="utf-8") as f:
    for line in f:                      # best for big files: one line at a time
        print(line.rstrip("\n"))

with open(p, encoding="utf-8") as f:
    print([line.strip().upper() for line in f])

with open(p, encoding="utf-8") as f:
    print(f.read().splitlines())        # lines without the newline characters

with open(p, encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number:>3}: {line.rstrip()}")

with open(p, encoding="utf-8") as f:
    f.read()
    print(repr(f.readline()))           # '' means end of file

print(p.read_text(encoding="utf-8").count("a"))   # the shortcut for small files