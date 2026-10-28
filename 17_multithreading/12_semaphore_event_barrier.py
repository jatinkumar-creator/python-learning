import threading
import time

# 1. Semaphore: at most N threads inside a block (a limited resource, such as 2 connections)
sem = threading.Semaphore(2)
count_lock = threading.Lock()
active = 0
peak = 0

def job(i):
    global active, peak
    with sem:
        with count_lock:
            active += 1
            peak = max(peak, active)
        time.sleep(0.3)
        with count_lock:
            active -= 1

start = time.perf_counter()
threads = [threading.Thread(target=job, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"semaphore: 10 jobs, peak concurrency {peak}, took {time.perf_counter() - start:.1f} s (about 5 x 0.3)")

# 2. Event used as a starting gun
go = threading.Event()
started = []

def runner(i):
    go.wait()                                # everyone blocks here
    started.append(i)

threads = [threading.Thread(target=runner, args=(i,)) for i in range(4)]
for t in threads:
    t.start()
time.sleep(0.3)
print("before go.set():", started)
go.set()
for t in threads:
    t.join()
print("after go.set()  :", sorted(started))

# 3. Event used as a stop flag: better than a global variable plus sleep
stop = threading.Event()

def ticker():
    n = 0
    while not stop.is_set():
        n += 1
        stop.wait(0.1)                       # sleeps 0.1 s, but wakes the instant stop is set
    print("  ticker stopped after", n, "ticks")

t = threading.Thread(target=ticker)
t.start()
time.sleep(0.55)
stop.set()
t.join()

# 4. Event.wait returns True/False
e = threading.Event()
print("wait(0.1) before set:", e.wait(0.1))
e.set()
print("wait(0.1) after set :", e.wait(0.1))
e.clear()
print("is_set after clear  :", e.is_set())

# 5. Barrier: everyone waits until all have arrived
barrier = threading.Barrier(3)

def racer(name, delay):
    time.sleep(delay)
    print(f"  {name} arrived")
    barrier.wait()
    print(f"  {name} released")

threads = [threading.Thread(target=racer, args=(n, d))
           for n, d in (("fast", 0.0), ("medium", 0.2), ("slow", 0.4))]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 6. BoundedSemaphore refuses extra releases
b = threading.BoundedSemaphore(1)
try:
    b.release()
except ValueError as e:
    print("ValueError:", e)