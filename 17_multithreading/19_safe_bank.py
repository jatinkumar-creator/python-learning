import random
import threading
import time

class Account:
    def __init__(self, ident, balance):
        self.ident = ident
        self.balance = balance
        self.lock = threading.Lock()

def transfer_unsafe(src, dst, amount):
    if src is dst:
        return False
    if src.balance >= amount:
        current = src.balance
        time.sleep(0)                           # exposes the race
        src.balance = current - amount
        current = dst.balance
        time.sleep(0)
        dst.balance = current + amount
        return True
    return False

def transfer_safe(src, dst, amount):
    if src is dst:                              # the same non-reentrant lock twice would deadlock
        return False
    first, second = sorted((src, dst), key=lambda a: a.ident)    # ALWAYS lock in the same order
    with first.lock, second.lock:
        if src.balance >= amount:
            src.balance -= amount
            dst.balance += amount
            return True
    return False

def simulate(transfer, label, accounts=5, threads=6, rounds=300):
    accts = [Account(i, 1000) for i in range(accounts)]
    before = sum(a.balance for a in accts)

    def worker(seed):
        rng = random.Random(seed)
        for _ in range(rounds):
            src, dst = rng.sample(accts, 2)
            transfer(src, dst, rng.randint(1, 200))

    pool = [threading.Thread(target=worker, args=(s,)) for s in range(threads)]
    for t in pool:
        t.start()
    for t in pool:
        t.join()
    after = sum(a.balance for a in accts)
    status = "OK" if before == after and min(a.balance for a in accts) >= 0 else "BROKEN"
    print(f"{label:<8} total before {before}, after {after}, lowest balance "
          f"{min(a.balance for a in accts)}   {status}")

simulate(transfer_unsafe, "unsafe")
simulate(transfer_safe, "safe")