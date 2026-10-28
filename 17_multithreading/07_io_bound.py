import threading
import time

def fetch(i):
    time.sleep(1)                 # stands in for a network request or a disk read
    return i

start = time.perf_counter()
for i in range(5):
    fetch(i)
print(f"sequential   : {time.perf_counter() - start:.2f} s")

start = time.perf_counter()
threads = [threading.Thread(target=fetch, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"5 threads    : {time.perf_counter() - start:.2f} s")