# nums = [1, 2, 3]
# print(nums[3])                       # IndexError

# [1, 2].remove(9)                     # ValueError

# [].pop()                             # IndexError

# t = (1, 2, 3)
# t[0] = 10                            # TypeError: tuples are immutable

# d = {"a": 1}
# print(d["b"])                        # KeyError

# d = {[1, 2]: "a"}                    # TypeError: unhashable type

# s = {1, 2, 3}
# print(s[0])                          # TypeError: sets have no indexing

# empty = {}
# empty.add(1)                         # AttributeError: that is a dict

# fs = frozenset([1, 2])
# fs.add(3)                            # AttributeError

# nums = [3, 1, 2]
# nums = nums.sort()
# print(nums[0])                       # TypeError: 'NoneType' is not subscriptable

# d = {1: "a", 2: "b"}
# for k in d:
#     d[k + 10] = "x"                  # RuntimeError: dictionary changed size