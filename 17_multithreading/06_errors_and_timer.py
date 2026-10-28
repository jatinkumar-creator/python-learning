import threading
import time

# 1. An exception inside a thread does NOT reach the main thread
def boom():
    raise ValueError("inside a worker thread")

t = threading.Thread(target=boom, name="Boomer")
t.start()
t.join()
print("main continues; the traceback above went to stderr\n")

# 2. Catch it centrally with threading.excepthook
caught = []

def hook(args):
    caught.append((args.thread.name, args.exc_type.__name__, str(args.exc_value)))

threading.excepthook = hook
t = threading.Thread(target=boom, name="Boomer2")
t.start()
t.join()
threading.excepthook = threading.__excepthook__            # restore the default
print("hook caught:", caught)

# 3. A thread class that keeps its result or its error
class ResultThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self._func, self._fargs, self._fkwargs = func, args, kwargs
        self.result = None
        self.error = None

    def run(self):
        try:
            self.result = self._func(*self._fargs, **self._fkwargs)
        except Exception as e:
            self.error = e

    def get(self):
        self.join()
        if self.error is not None:
            raise self.error
        return self.result

good = ResultThread(pow, 2, 10)
bad = ResultThread(int, "abc")
good.start()
bad.start()
print("good:", good.get())
try:
    bad.get()
except ValueError as e:
    print("bad raised in the caller:", e)

# 4. Timer: run something once, later
def hello():
    print("  timer fired")

timer = threading.Timer(0.3, hello)
timer.start()
timer.join()

cancelled = threading.Timer(5, hello)
cancelled.start()
cancelled.cancel()
cancelled.join()
print("the cancelled timer never fired")