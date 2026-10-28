import multiprocessing as mp
import os
import threading

shared_list = []

def in_thread():
    shared_list.append(("thread", os.getpid()))

def in_process(queue):
    shared_list.append(("process", os.getpid()))      # changes the CHILD's own copy only
    queue.put(("child sees", list(shared_list)))

if __name__ == "__main__":
    print("parent pid:", os.getpid())

    t = threading.Thread(target=in_thread)
    t.start()
    t.join()
    print("after thread :", shared_list)

    q = mp.Queue()
    p = mp.Process(target=in_process, args=(q,))
    p.start()
    print(q.get())
    p.join()
    print("after process:", shared_list)
    print("exit code    :", p.exitcode)