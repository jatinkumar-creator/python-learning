from collections import deque
from itertools import islice

def batches(iterable, size):
    it = iter(iterable)
    while batch := list(islice(it, size)):
        yield batch

def sliding_window(iterable, n):
    window = deque(maxlen=n)
    for x in iterable:
        window.append(x)
        if len(window) == n:
            yield tuple(window)

def moving_average(values, n):
    return (sum(w) / n for w in sliding_window(values, n))

print(list(batches(range(7), 3)))
print(list(sliding_window([1, 2, 3, 4, 5], 3)))
print(list(moving_average([10, 20, 30, 40, 50], 3)))
print(list(batches("abcdefg", 2)))
print(list(batches(x * x for x in range(5)), ))     # works on a generator too