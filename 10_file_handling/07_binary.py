import hashlib
from common import SCRATCH

src = SCRATCH / "data.bin"
dst = SCRATCH / "data_copy.bin"

data = bytes(range(256)) * 4
with open(src, "wb") as f:
    print("wrote", f.write(data), "bytes")

with open(src, "rb") as f:
    head = f.read(8)
print(head, list(head), type(head), head[0])

def copy_in_chunks(a, b, size=64):
    with open(a, "rb") as fin, open(b, "wb") as fout:
        while chunk := fin.read(size):
            fout.write(chunk)

copy_in_chunks(src, dst)

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

print(sha256_of(src)[:16], sha256_of(dst)[:16])
print("identical copy:", sha256_of(src) == sha256_of(dst))

# bytes are immutable, bytearray is mutable
ba = bytearray(b"abc")
ba[0] = 65
print(ba, bytes(ba))
try:
    b"abc"[0] = 65
except TypeError as e:
    print("TypeError:", e)

# Opening binary data in text mode
try:
    with open(src, encoding="utf-8") as f:
        f.read()
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)