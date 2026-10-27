from common import SCRATCH

p = SCRATCH / "seek.txt"

with open(p, "w+", encoding="utf-8") as f:
    f.write("0123456789")
    print("tell after write:", f.tell())
    f.seek(0)
    print(f.read(3), f.tell())
    f.seek(5)
    print(f.read(2))
    f.seek(0, 2)                        # 2 means "from the end" (offset must be 0 in text mode)
    print("end position:", f.tell())
    f.seek(4)
    f.truncate()                        # cut the file at the current position
    f.seek(0)
    print(repr(f.read()))
    try:
        f.seek(-3, 2)
    except Exception as e:
        print(type(e).__name__ + ":", e)

# Binary mode allows relative seeks
with open(p, "rb") as f:
    f.seek(-2, 2)                       # 2 bytes before the end
    print(f.read())
    f.seek(1)
    f.seek(1, 1)                        # 1 means "from the current position"
    print(f.read(1))

# Overwrite in the middle with r+
p.write_text("abcdef", encoding="utf-8")
with open(p, "r+", encoding="utf-8") as f:
    f.write("XY")                       # overwrites, does not insert
print(p.read_text(encoding="utf-8"))