# import threading
# t = threading.Thread(target=print)
# t.join()                                       # RuntimeError: cannot join thread before it is started

# import threading
# threading.current_thread().join()              # RuntimeError: cannot join current thread

# import threading
# class Bad(threading.Thread):
#     def __init__(self):
#         pass                                    # forgot super().__init__()
# Bad().start()                                  # RuntimeError: thread.__init__() not called

# import threading
# threading.Lock().release()                     # RuntimeError: release unlocked lock

# import threading
# threading.BoundedSemaphore(1).release()        # ValueError: Semaphore released too many times

# import queue
# queue.Queue().get_nowait()                     # queue.Empty

# import queue
# q = queue.Queue(maxsize=1)
# q.put(1)
# q.put_nowait(2)                                # queue.Full

# import threading
# t = threading.Thread(target=print, daemon=True)
# t.start()
# t.daemon = False                               # RuntimeError: cannot set daemon status of active thread

# import threading
# def work(a, b):
#     print(a, b)
# t = threading.Thread(target=work, args=(1,))
# t.start()                                      # TypeError INSIDE the thread: the traceback prints, the main thread continues
# t.join()
# print("main is still alive")




#Careful with this one (Windows). If you ever need to stop a runaway script, press Ctrl + C.
# import multiprocessing as mp
# def hello():
#     print("child says hello")
# p = mp.Process(target=hello)                   # no "if __name__ == '__main__':" guard
# p.start()                                      # RuntimeError: an attempt has been made to start a new process
# p.join()                                       # before the current process has finished its bootstrapping phase

# import multiprocessing as mp
# if __name__ == "__main__":
#     p = mp.Process(target=lambda: print("hi"))  # lambdas cannot be pickled for the new process
#     p.start()                                   # AttributeError / PicklingError: Can't pickle local object

#Silent traps (no error at all):
# 1. Reading results before join(): the numbers are incomplete
# import threading, time
# results = []
# def work(n):
#     time.sleep(0.2)
#     results.append(n)
# threads = [threading.Thread(target=work, args=(i,)) for i in range(3)]
# for t in threads: t.start()
# print(results)                                  # [] because nothing has finished yet
# for t in threads: t.join()
# print(sorted(results))

# 2. Starting and joining inside the same loop makes the threads run one at a time
# for i in range(3):
#     t = threading.Thread(target=work, args=(i,)); t.start(); t.join()    # no concurrency at all