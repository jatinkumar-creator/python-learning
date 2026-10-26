import timeit

big_list = list(range(100_000))
big_set = set(big_list)

print("list:", timeit.timeit("99_999 in big_list", globals=globals(), number=1000))
print("set :", timeit.timeit("99_999 in big_set", globals=globals(), number=1000))