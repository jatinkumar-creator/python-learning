# bool is a subclass of int
print(True + True, True * 5, isinstance(True, int), True == 1)

# truthiness
for v in [0, 1, "", "0", " ", None, [], [0], 0.0, "False"]:
    print(repr(v), "->", bool(v))

print(all([]), any([]), all([1, 2]), any([0, 3]))

# None
x = None
print(type(x), x is None, x == False, bool(x))

def f():
    pass
print(f())                                # functions return None by default

# The classic None bug
nums = [3, 1, 2]
result = nums.sort()
print(result, nums)
nums = [3, 1, 2]
print(sorted(nums), nums)                 # sorted() returns a new list