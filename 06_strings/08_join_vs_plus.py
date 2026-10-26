import timeit

setup = "parts = [str(i) for i in range(50_000)]"
loop = """
s = ''
for p in parts:
    s += p
"""
print("+= loop:", timeit.timeit(loop, setup=setup, number=20))
print("join   :", timeit.timeit("''.join(parts)", setup=setup, number=20))