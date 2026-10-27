from collections import Counter, deque
from datetime import datetime
from common import SCRATCH

LOG = SCRATCH / "app.log"

def log(level, message):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{stamp} [{level}] {message}\n")

def tail(n=3):
    with open(LOG, encoding="utf-8") as f:
        return list(deque(f, maxlen=n))         # keeps only the last n lines in memory

log("INFO", "program started")
log("WARNING", "disk almost full")
log("ERROR", "could not open config")
log("INFO", "program finished")

for line in tail(3):
    print(line, end="")

with open(LOG, encoding="utf-8") as f:
    counts = Counter(line.split("[")[1].split("]")[0] for line in f)
print(counts)