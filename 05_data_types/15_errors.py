# t = (1, 2, 3)
# t[0] = 10                         # TypeError: tuples are immutable

# s = "hello"
# s[0] = "J"                        # TypeError: strings are immutable

# d = {[1, 2]: "a"}                 # TypeError: unhashable type: 'list'

# empty = {}
# empty.add(1)                      # AttributeError: it's a dict, not a set

# d = {"a": 1}
# print(d["b"])                     # KeyError

# nums = [3, 1, 2]
# nums = nums.sort()
# print(nums[0])                    # TypeError: 'NoneType' is not subscriptable

# s = {1, 2, 3}
# print(s[0])                       # TypeError: sets have no indexing

# print("Age: " + 28)               # TypeError: can't concatenate str and int