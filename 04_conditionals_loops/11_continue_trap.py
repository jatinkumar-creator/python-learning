# This version is correct: update the counter BEFORE continue
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print()

# Try removing "i += 1" before continue to see an infinite loop.
# Stop it with Ctrl + C.