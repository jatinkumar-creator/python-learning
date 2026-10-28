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