import queue
import threading
import time

# 1. Producer / consumer with a bounded queue
q = queue.Queue(maxsize=3)           # put() blocks while the queue is full
CONSUMERS = 2
SENTINEL = None                      # a "no more work" marker
results = []
results_lock = threading.Lock()

def producer(n):
    for i in range(n):
        q.put(i)
    for _ in range(CONSUMERS):
        q.put(SENTINEL)              # one stop marker per consumer

def consumer(name):
    while True:
        item = q.get()               # blocks until something arrives
        try:
            if item is SENTINEL:
                return
            time.sleep(0.05)
            with results_lock:
                results.append((item, item * item, name))
        finally:
            q.task_done()            # always report the item as handled

threads = [threading.Thread(target=producer, args=(8,))]
threads += [threading.Thread(target=consumer, args=(f"C{i}",)) for i in range(CONSUMERS)]
for t in threads:
    t.start()
q.join()                             # waits until every item has been task_done()
for t in threads:
    t.join()
for item, square, name in sorted(results):
    print(f"  item {item} -> {square:>2}  handled by {name}")

# 2. The other queue types
fifo, lifo, prio = queue.Queue(), queue.LifoQueue(), queue.PriorityQueue()
for item in (3, 1, 2):
    fifo.put(item)
    lifo.put(item)
prio.put((3, "low"))
prio.put((1, "urgent"))
prio.put((2, "normal"))
print("FIFO:", [fifo.get() for _ in range(3)])
print("LIFO:", [lifo.get() for _ in range(3)])
print("Priority:", [prio.get() for _ in range(3)])

# 3. Empty and Full
try:
    queue.Queue().get_nowait()
except queue.Empty:
    print("queue.Empty from get_nowait()")
try:
    queue.Queue().get(timeout=0.2)
except queue.Empty:
    print("queue.Empty after a 0.2 s timeout")
full = queue.Queue(maxsize=1)
full.put("x")
try:
    full.put_nowait("y")
except queue.Full:
    print("queue.Full from put_nowait()")

# 4. Condition: wait until something is true
cond = threading.Condition()
items = []

def waiter():
    with cond:
        while not items:             # ALWAYS re-check in a while loop
            cond.wait()              # releases the lock while waiting
        print("  waiter got:", items.pop())

def setter():
    time.sleep(0.3)
    with cond:
        items.append("data")
        cond.notify()

w = threading.Thread(target=waiter)
s = threading.Thread(target=setter)
w.start()
s.start()
w.join()
s.join()