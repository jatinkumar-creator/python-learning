with open("out.txt", "w") as f:
    print("Saved with print()", file=f)
    print("Second line", file=f)

with open("out.txt") as f:
    print(f.read())