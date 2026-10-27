import tracemalloc
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)
big = SCRATCH / "big.txt"

with open(big, "w", encoding="utf-8") as f:
    for i in range(200_000):
        f.write(f"line {i} {'ERROR' if i % 1000 == 0 else 'ok'}\n")

def matching(path, word):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if word in line:
                yield line.rstrip("\n")

hits = matching(big, "ERROR")
print(next(hits))
print(sum(1 for _ in hits) + 1, "matches in total")

tracemalloc.start()
count = sum(1 for _ in matching(big, "ERROR"))
print("streaming :", count, f"matches, peak {tracemalloc.get_traced_memory()[1] / 1024:.0f} KiB")

tracemalloc.reset_peak()
lines = big.read_text(encoding="utf-8").splitlines()
matches = [line for line in lines if "ERROR" in line]
print("loading   :", len(matches), f"matches, peak {tracemalloc.get_traced_memory()[1] / 1024:.0f} KiB")
tracemalloc.stop()