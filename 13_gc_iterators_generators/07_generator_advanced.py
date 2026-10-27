from itertools import chain, count, cycle, islice, takewhile

# 1. Infinite sequences, taken lazily with islice
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(islice(fib(), 10)))
print(list(takewhile(lambda x: x < 50, fib())))

def primes():
    found = []
    for n in count(2):
        if all(n % p for p in found if p * p <= n):
            found.append(n)
            yield n

print(list(islice(primes(), 10)))

# 2. yield from: delegate to another iterable or generator
def chain_two(a, b):
    yield from a
    yield from b

print(list(chain_two([1, 2], "ab")))

def flatten(items):
    for item in items:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)              # recursion with generators
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], (5, 6), 7])))

def sub():
    yield 1
    return "sub result"

def outer():
    result = yield from sub()                     # captures the sub-generator's return value
    print("sub returned:", result)
    yield 2

print(list(outer()))

# 3. send(): push values INTO a generator (a coroutine-style generator)
def running_average():
    total, n, average = 0, 0, None
    while True:
        value = yield average
        total += value
        n += 1
        average = total / n

avg = running_average()
next(avg)                                         # "prime" it: run to the first yield
print(avg.send(10), avg.send(20), avg.send(60))

# 4. close(): stop a generator and run its cleanup
def resource():
    print("open")
    try:
        while True:
            yield "data"
    finally:
        print("cleanup")

r = resource()
print(next(r))
r.close()
try:
    next(r)
except StopIteration:
    print("closed generators are finished")

# 5. itertools: lazy building blocks
print(list(islice(cycle("ab"), 5)))
print(list(chain([1, 2], [3], (4,))))
print(list(islice(count(10, 5), 4)))