# 1. A class that is its OWN iterator: remembers its position, usable once
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

c = Countdown(3)
print(list(c), list(c))              # the second pass is empty

# 2. An iterable that hands out a FRESH iterator each time: reusable
class CountdownIterable:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return Countdown(self.start)

cd = CountdownIterable(3)
print(list(cd), list(cd))

# 3. The easiest way: let __iter__ be a generator function
class Evens:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        for n in range(0, self.limit, 2):
            yield n

e = Evens(10)
print(list(e), list(e), 4 in e, 5 in e)     # "in" works by iterating
print(sum(e), max(e), sorted(e, reverse=True))

# 4. Wrapping a collection
class Playlist:
    def __init__(self, *songs):
        self.songs = list(songs)

    def __iter__(self):
        return iter(self.songs)

    def __len__(self):
        return len(self.songs)

pl = Playlist("A", "B", "C")
for i, song in enumerate(pl, start=1):
    print(i, song)
a, b, c = pl                                 # unpacking works with any iterable
print(a, b, c, len(pl), list(pl))

# 5. A lazy iterator over a sequence in pairs
class Pairs:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        for i in range(0, len(self.items) - 1, 2):
            yield self.items[i], self.items[i + 1]

print(list(Pairs([1, 2, 3, 4, 5, 6])))
print(dict(Pairs(["a", 1, "b", 2])))