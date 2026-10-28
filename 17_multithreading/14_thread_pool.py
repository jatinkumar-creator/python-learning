import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    time.sleep(0.2 * (5 - n))        # higher numbers finish SOONER
    if n == 3:
        raise ValueError(f"task {n} failed")
    return n * n

# 1. submit + as_completed: results arrive in FINISH order, errors surface on result()
with ThreadPoolExecutor(max_workers=5) as ex:
    futures = {ex.submit(task, n): n for n in range(5)}
    for fut in as_completed(futures):
        n = futures[fut]
        try:
            print(f"  task {n} -> {fut.result()}")
        except ValueError as e:
            print(f"  task {n} raised ValueError: {e}")

# 2. map: results in INPUT order; an error is raised when you reach it
def square_slowly(n):
    time.sleep(0.2)
    return n * n

with ThreadPoolExecutor(max_workers=4) as ex:
    print("map:", list(ex.map(square_slowly, [1, 2, 3, 4])))

# 3. Speed-up
start = time.perf_counter()
for n in range(10):
    square_slowly(n)
sequential = time.perf_counter() - start

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as ex:
    list(ex.map(square_slowly, range(10)))
pooled = time.perf_counter() - start
print(f"sequential {sequential:.2f} s, pool of 5 {pooled:.2f} s")

# 4. Timeouts and done()
with ThreadPoolExecutor(max_workers=1) as ex:
    fut = ex.submit(time.sleep, 0.5)
    print("done right away:", fut.done())
    try:
        fut.result(timeout=0.1)
    except TimeoutError:
        print("TimeoutError: the task is still running (it was not cancelled)")
    fut.result()
    print("done now:", fut.done())

# 5. A callback when a future finishes
with ThreadPoolExecutor(max_workers=2) as ex:
    fut = ex.submit(square_slowly, 7)
    fut.add_done_callback(lambda f: print("  callback got:", f.result()))