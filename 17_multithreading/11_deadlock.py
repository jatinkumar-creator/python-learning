import threading
import time

a, b = threading.Lock(), threading.Lock()

def worker(name, first, second, log):
    with first:
        time.sleep(0.2)                      # now both threads hold their first lock
        if second.acquire(timeout=1):        # a real program would wait here forever
            log.append(f"{name}: got both locks")
            second.release()
        else:
            log.append(f"{name}: gave up waiting, DEADLOCK")

def run(label, order1, order2):
    log = []
    t1 = threading.Thread(target=worker, args=("T1", *order1, log))
    t2 = threading.Thread(target=worker, args=("T2", *order2, log))
    start = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"{label} ({time.perf_counter() - start:.1f} s)")
    for line in sorted(log):
        print("  ", line)

run("opposite lock order", (a, b), (b, a))
run("same lock order    ", (a, b), (a, b))