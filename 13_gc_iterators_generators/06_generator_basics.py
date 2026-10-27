import sys

def count_up(n):
    print("generator starts")
    for i in range(1, n + 1):
        print(f"  about to yield {i}")
        yield i
    print("generator finishing")

g = count_up(3)
print(type(g))
print("created: nothing has run yet")
print(next(g))
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration as e:
    print("StopIteration, value:", e.value)

# A return value rides on StopIteration
def with_result():
    yield 1
    yield 2
    return "finished"

g = with_result()
next(g)
next(g)
try:
    next(g)
except StopIteration as e:
    print("return value:", e.value)

# One pass only
g = (x * x for x in range(3))
print(list(g), list(g))

# Generator expression vs list comprehension
big_list = [x for x in range(1_000_000)]
big_gen = (x for x in range(1_000_000))
print(sys.getsizeof(big_list), sys.getsizeof(big_gen))
print(sum(x for x in range(1_000_000)))        # no million-item list ever exists

# A generator only does the work you ask for
def noisy_squares(n):
    for i in range(n):
        print("computing", i)
        yield i * i

for sq in noisy_squares(10):
    if sq > 10:
        break
    print("got", sq)

# State lives in local variables between yields
def counter():
    n = 0
    while True:                                # an infinite generator is fine
        n += 1
        yield n

c1, c2 = counter(), counter()
print(next(c1), next(c1), next(c1), next(c2))   # independent states

# A generator is a function, so it can take arguments and call other functions
def evens_up_to(limit):
    return (n for n in range(limit) if n % 2 == 0)

print(list(evens_up_to(10)))