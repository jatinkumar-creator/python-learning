import time

x = print("hi")
print(x)                       # what does print() return?

for i in range(3, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
print("Go!")