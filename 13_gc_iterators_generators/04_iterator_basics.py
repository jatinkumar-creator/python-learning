nums = [10, 20, 30]
it = iter(nums)
print(type(nums).__name__, type(it).__name__)
print(next(it), next(it), next(it))

try:
    next(it)
except StopIteration:
    print("StopIteration: nothing left")

print(list(it))                     # an exhausted iterator stays empty
print(next(it, "default"))          # a default value avoids the exception

# What a for loop really does
it = iter(nums)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print("item:", item)

# An iterator returns itself from iter(); a list returns a NEW iterator each time
it = iter(nums)
print(iter(it) is it, iter(nums) is nums, iter(nums) is iter(nums))

# Many things are iterable
for thing in ["abc", (1, 2), {1, 2}, {"k": "v"}, range(2)]:
    print(type(thing).__name__, list(iter(thing)))

# Stopping a for loop early leaves the iterator where it stopped
it = iter(range(5))
for x in it:
    if x == 2:
        break
print(list(it))

# The two-argument form: iter(callable, sentinel)
data = iter([3, 2, 1, 0, 5])
print(list(iter(lambda: next(data), 0)))     # stops when the callable returns 0

# Tools that consume iterators
print(sum(iter([1, 2, 3])), max(iter([4, 9, 2])), sorted(iter("cab")), list(zip("ab", [1, 2])))

# enumerate, zip, map, filter and reversed return iterators, not lists
e = enumerate("ab")
m = map(str.upper, "ab")
print(type(e).__name__, type(m).__name__, list(m), list(m))

# Is it iterable? Is it an iterator?
from collections.abc import Iterable, Iterator
for obj in ([1], iter([1]), 5, "text", (x for x in range(1))):
    print(f"{type(obj).__name__:<18} iterable={isinstance(obj, Iterable)!s:<6} iterator={isinstance(obj, Iterator)}")