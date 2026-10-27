from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map: apply a function to every item (returns a lazy iterator)
print(list(map(lambda n: n * n, nums)))
print(list(map(str.upper, ["a", "b"])))
print(list(map(lambda x, y: x + y, [1, 2], [10, 20])))
print(list(map(int, "1 2 3".split())))
m = map(lambda n: n * 2, nums)
print(type(m), list(m), list(m))        # an iterator is used up after one pass

# filter: keep the items where the function returns True
print(list(filter(lambda n: n % 2 == 0, nums)))
print(list(filter(None, [0, 1, "", 2, None, "x"])))   # None means "keep truthy items"

# reduce: fold a sequence into one value
print(reduce(lambda a, b: a + b, nums))
print(reduce(lambda a, b: a * b, nums))
print(reduce(lambda a, b: a + b, [], 0))             # the initial value handles an empty list
print(reduce(max, [3, 9, 2]))

# any / all
print(any([0, "", None]), any([0, 1]), any([]))
print(all([1, 2, 3]), all([1, 0]), all([]))
print(any(n > 5 for n in nums), all(n > 0 for n in nums))
print(any(c.isdigit() for c in "abc1"), all(c.isalpha() for c in "abc1"))

# Lambda
square = lambda x: x * x
print(square(5), (lambda x, y=2: x ** y)(3))
print(sorted(["banana", "kiwi", "apple"], key=lambda w: len(w)))
print(max([("a", 3), ("b", 7)], key=lambda p: p[1]))

# Same results with comprehensions
print([n * n for n in nums])
print([n for n in nums if n % 2 == 0])