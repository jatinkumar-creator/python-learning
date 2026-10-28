import hashlib
import os
import shutil
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DIR = Path(__file__).resolve().parent / "scratch" / "hash_demo"
DIR.mkdir(parents=True, exist_ok=True)
FILES, SIZE = 6, 8 * 1024 * 1024
for i in range(FILES):
    (DIR / f"file{i}.bin").write_bytes(os.urandom(SIZE))

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return path.name, h.hexdigest()

paths = sorted(DIR.glob("*.bin"))

start = time.perf_counter()
sequential = [sha256_of(p) for p in paths]
t_seq = time.perf_counter() - start

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as ex:
    threaded = list(ex.map(sha256_of, paths))             # map keeps the input order
t_thr = time.perf_counter() - start

print(f"sequential {t_seq:.2f} s, threads {t_thr:.2f} s")
print("same results:", sequential == threaded)
for name, digest in threaded[:3]:
    print(f"  {name}  {digest[:16]}...")

shutil.rmtree(DIR)                                        # remove the 48 MB of test files
print("cleaned up:", not DIR.exists())