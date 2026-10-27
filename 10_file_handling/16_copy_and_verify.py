import hashlib
import shutil
from common import SCRATCH

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

src = SCRATCH / "original.txt"
dst = SCRATCH / "backup.txt"
src.write_text("Important data\n" * 1000, encoding="utf-8")

shutil.copy2(src, dst)                         # copy2 also keeps the timestamps
if sha256_of(src) == sha256_of(dst):
    print("Backup verified: identical")
else:
    print("Backup FAILED: files differ")

with open(dst, "a", encoding="utf-8") as f:    # tamper with the copy
    f.write("one extra line\n")

print("After tampering:", "identical" if sha256_of(src) == sha256_of(dst) else "DIFFERENT")