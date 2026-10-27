# next([1, 2, 3])                        # TypeError: 'list' object is not an iterator

# iter(5)                                # TypeError: 'int' object is not iterable

# g = (x for x in range(3))
# g[0]                                   # TypeError: 'generator' object is not subscriptable

# len(x for x in range(3))               # TypeError: object of type 'generator' has no len()

# def gen():
#     yield 1
# g = gen()
# g.send("hi")                           # TypeError: can't send non-None value to a just-started generator

# def g():
#     yield next(gen)
# gen = g()
# next(gen)                              # ValueError: generator already executing

# def bad():
#     yield 1
#     raise StopIteration
# list(bad())                            # RuntimeError: generator raised StopIteration

# class NotAnIterator:
#     def __iter__(self):
#         return self                      # but there is no __next__
# list(NotAnIterator())                  # TypeError: iter() returned non-iterator

# import weakref
# weakref.ref(5)                         # TypeError: cannot create weak reference to 'int' object

# from pathlib import Path
# p = Path(__file__).parent / "scratch" / "big.txt"
# def lines_wrong(path):
#     with open(path, encoding="utf-8") as f:
#         return (line for line in f)    # the file closes when the function returns!
# next(lines_wrong(p))                   # ValueError: I/O operation on closed file