import threading

lock = threading.Lock()

# 1. The methods
print("locked at start      :", lock.locked())
lock.acquire()
print("locked after acquire :", lock.locked())
print("second acquire, non-blocking:", lock.acquire(blocking=False))
print("second acquire, timeout 0.3 :", lock.acquire(timeout=0.3))
lock.release()
print("locked after release :", lock.locked())

try:
    lock.release()
except RuntimeError as e:
    print("RuntimeError:", e)

# 2. "with" releases the lock even when an error happens
try:
    with lock:
        raise ValueError("oops inside the lock")
except ValueError:
    pass
print("released after the error:", not lock.locked())

# 3. A plain Lock cannot be taken twice by the same thread. An RLock can
rlock = threading.RLock()

def nested(l):
    with l:
        with l:
            return "acquired twice by the same thread"

print("RLock:", nested(rlock))

plain = threading.Lock()
plain.acquire()
print("plain Lock, same thread, again:", plain.acquire(timeout=0.3), "(it would wait forever without the timeout)")
plain.release()

# 4. When you need an RLock: methods that call each other and both lock
class Counter:
    def __init__(self):
        self._lock = threading.RLock()
        self.value = 0

    def add(self, n):
        with self._lock:
            self.value += n

    def add_twice(self, n):
        with self._lock:              # holds the lock...
            self.add(n)               # ...and add() takes it again
            self.add(n)

c = Counter()
c.add_twice(5)
print("value:", c.value)

# 5. Lock objects are shared, so every thread must use the SAME one
a, b = threading.Lock(), threading.Lock()
print("different locks protect nothing from each other:", a is not b)