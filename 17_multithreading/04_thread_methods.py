import threading
import time

def slow(seconds):
    time.sleep(seconds)

# 1. Attributes and join(timeout)
t = threading.Thread(target=slow, args=(1.0,), name="Slow")
print("before start:", t.name, t.ident, t.native_id, t.daemon, t.is_alive())
t.start()
print("after start :", t.ident is not None, t.native_id is not None, t.is_alive())
t.join(timeout=0.2)
print("join(0.2) returned, but alive is still:", t.is_alive())
t.join()
print("after full join, alive:", t.is_alive())

# 2. Counting and listing threads
workers = [threading.Thread(target=slow, args=(0.5,), name=f"W{i}") for i in range(3)]
for w in workers:
    w.start()
print("active_count:", threading.active_count())
print("names       :", sorted(x.name for x in threading.enumerate()))
for w in workers:
    w.join()
print("active_count after joins:", threading.active_count())

# 3. daemon cannot be changed after start
d = threading.Thread(target=slow, args=(0.3,), daemon=True)
d.start()
try:
    d.daemon = False
except RuntimeError as e:
    print("RuntimeError:", e)
d.join()

# 4. A thread can ask who it is
def whoami():
    me = threading.current_thread()
    print(f"  I am {me.name!r}, ident {me.ident}, main thread? {me is threading.main_thread()}")

for name in ("A", "B"):
    x = threading.Thread(target=whoami, name=name)
    x.start()
    x.join()

# 5. Thread-local data: every thread sees its own value
local = threading.local()

def store(value):
    local.value = value
    time.sleep(0.05)
    print(f"  {threading.current_thread().name} sees {local.value}")

threads = [threading.Thread(target=store, args=(i,), name=f"L{i}") for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("main thread has 'value':", hasattr(local, "value"))