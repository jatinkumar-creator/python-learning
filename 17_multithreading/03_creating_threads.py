import threading

def greet(name, greeting="Hello"):
    print(f"  [{threading.current_thread().name}] {greeting}, {name}!")

# 1. target, args, kwargs, name
t = threading.Thread(target=greet, args=("Asha",), kwargs={"greeting": "Hi"}, name="Greeter")
print("before start, alive:", t.is_alive())
t.start()
t.join()
print("after join, alive:", t.is_alive())

# 2. Trap: args must be a TUPLE. ("Asha") is just a string
print("--- args trap ---")
t = threading.Thread(target=greet, args=("Asha"))      # becomes greet("A", "s", "h", "a")
t.start()
t.join()
print("the error above happened inside the thread; the main thread carries on")
t = threading.Thread(target=greet, args=("Asha",))     # the comma makes the tuple
t.start()
t.join()

# 3. Trap: target=greet("Asha") CALLS the function right now, in the main thread
print("--- call trap ---")
t = threading.Thread(target=greet("Asha"))             # greet() already ran; its result, None, is the target
t.start()
t.join()

# 4. A subclass that overrides run()
class Countdown(threading.Thread):
    def __init__(self, start_from):
        super().__init__(name=f"Countdown-{start_from}")   # forget this and start() fails
        self.start_from = start_from
        self.result = None

    def run(self):
        self.result = sum(range(self.start_from, 0, -1))

c = Countdown(100)
c.start()
c.join()
print(c.name, "->", c.result)

# 5. A thread can be started only once
t = threading.Thread(target=lambda: None)
t.start()
t.join()
try:
    t.start()
except RuntimeError as e:
    print("RuntimeError:", e)

# 6. run() called directly does NOT create a thread
def who():
    print("  running in:", threading.current_thread().name)

t = threading.Thread(target=who, name="Child")
t.run()                      # runs in the MAIN thread
t.start()                    # runs in "Child"
t.join()

# 7. Collecting results from several threads
results = {}

def square(n):
    results[n] = n * n

threads = [threading.Thread(target=square, args=(n,)) for n in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(sorted(results.items()))