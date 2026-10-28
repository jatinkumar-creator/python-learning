import sys
import threading
import time

daemon = len(sys.argv) > 1 and sys.argv[1] == "daemon"

def ticker():
    for i in range(1, 6):
        print("  tick", i, flush=True)
        time.sleep(0.3)
    print("  ticker finished cleanly", flush=True)

t = threading.Thread(target=ticker, daemon=daemon)
t.start()
time.sleep(0.7)
print("main finished; daemon =", daemon, flush=True)