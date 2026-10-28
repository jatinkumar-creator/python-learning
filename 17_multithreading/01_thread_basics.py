import os
import threading

print("process id      :", os.getpid())
print("current thread  :", threading.current_thread().name)
print("main thread     :", threading.main_thread().name)
print("current is main :", threading.current_thread() is threading.main_thread())
print("thread ident    :", threading.get_ident())
print("native id       :", threading.get_native_id())
print("active threads  :", threading.active_count())
print("CPU cores       :", os.cpu_count())

def worker():
    t = threading.current_thread()
    print(f"  in {t.name}: process id {os.getpid()}")

t = threading.Thread(target=worker, name="Worker-1")
t.start()
t.join()

# Threads share memory
shared = []

def add():
    shared.append(threading.current_thread().name)

threads = [threading.Thread(target=add, name=f"T{i}") for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("all three wrote into the same list:", sorted(shared))