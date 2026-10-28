import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# 1
def f():
    return 42

t = threading.Thread(target=f)
t.start()
t.join()
print(t.is_alive())

# 2
t = threading.Thread(target=lambda: None)
t.start()
t.join()
try:
    t.start()
except RuntimeError:
    print("RuntimeError")

# 3
t = threading.Thread(target=print, args=("hi",))
t.run()
print(t.is_alive())

# 4
print(threading.current_thread().name, threading.active_count())

# 5
results = []

def add(n):
    results.append(n)

ts = [threading.Thread(target=add, args=(i,)) for i in range(3)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(sorted(results))

# 6
l = threading.Lock()
print(l.locked(), l.acquire(), l.locked(), l.acquire(False))

# 7
r = threading.RLock()
print(r.acquire(), r.acquire(False))

# 8
e = threading.Event()
print(e.is_set(), e.wait(0.1))
e.set()
print(e.is_set(), e.wait(0.1))

# 9
fifo, lifo, prio = queue.Queue(), queue.LifoQueue(), queue.PriorityQueue()
for x in (1, 2, 3):
    fifo.put(x)
    lifo.put(x)
prio.put((3, "c"))
prio.put((1, "a"))
print(fifo.get(), lifo.get(), prio.get())

# 10
try:
    queue.Queue().get_nowait()
except queue.Empty:
    print("empty")

# 11
s = threading.Semaphore(2)
print(s.acquire(False), s.acquire(False), s.acquire(False))

# 12
try:
    threading.BoundedSemaphore(1).release()
except ValueError as err:
    print("ValueError:", err)

# 13
print(threading.Thread(target=f).daemon, threading.Thread(target=f, daemon=True).daemon)

# 14
with ThreadPoolExecutor(2) as ex:
    print(list(ex.map(lambda x: x * 2, [1, 2, 3])))
    print(ex.submit(pow, 2, 5).result())

# 15
count = 0
lock = threading.Lock()

def inc():
    global count
    for _ in range(1000):
        with lock:
            count += 1

ts = [threading.Thread(target=inc) for _ in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(count)

# 16
t = threading.Thread(target=time.sleep, args=(0.5,))
t.start()
t.join(0.1)
print(t.is_alive())
t.join()
print(t.is_alive())

# 17: a famous trap: args="ab" is NOT a tuple
t = threading.Thread(target=print, args=("ab"))
t.start()
t.join()

# 18
def boom():
    raise KeyError("lost")

fut_error = None
with ThreadPoolExecutor(1) as ex:
    fut = ex.submit(boom)
    try:
        fut.result()
    except KeyError as err:
        fut_error = err
print(type(fut_error).__name__, fut.exception() is fut_error)