import threading
import time

counter = 0

def unsafe(n):
    global counter
    for _ in range(n):
        current = counter            # 1. read
        time.sleep(0)                # 2. let other threads run: this exposes the race
        counter = current + 1        # 3. write back a possibly stale value

lock = threading.Lock()

def safe(n):
    global counter
    for _ in range(n):
        with lock:                   # only one thread at a time may run this block
            current = counter
            time.sleep(0)
            counter = current + 1

def plain_unsafe(n):
    global counter
    for _ in range(n):
        counter += 1                 # looks like one step, but it is read + add + write

def run(worker, label, threads=4, n=2000):
    global counter
    counter = 0
    pool = [threading.Thread(target=worker, args=(n,)) for _ in range(threads)]
    for t in pool:
        t.start()
    for t in pool:
        t.join()
    expected = threads * n
    verdict = "OK" if counter == expected else f"LOST {expected - counter} updates"
    print(f"{label:<26} expected {expected:>7}, got {counter:>7}   {verdict}")

run(unsafe, "unsafe (forced race)")
run(safe, "safe (with a Lock)")
for _ in range(3):
    run(plain_unsafe, "plain counter += 1", n=200_000)