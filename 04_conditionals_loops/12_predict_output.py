# 1
x = 0
if x:
    print("A")
else:
    print("B")

# 2
marks = 80
if marks >= 50:
    print("C")
elif marks >= 75:
    print("B")

# 3
for i in range(5):
    print(i, end=" ")
print()

# 4
print(list(range(10, 0, -3)), list(range(5, 1)))

# 5
for i in range(1, 10):
    if i % 3 == 0:
        break
    print(i, end=" ")
print()

# 6
for i in range(3):
    print(i)
else:
    print("Done")

# 7
for i in range(5):
    if i == 3:
        break
else:
    print("No break")
print("End")

# 8
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

# 9
for i in range(3):
    pass
print(i)

# 10
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    count += i
print(count)