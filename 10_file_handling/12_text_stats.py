from common import SCRATCH

path = SCRATCH / "sample.txt"
path.write_text("""Python makes file handling simple.
Open the file, read it, and close it.
Better: use a with block!
""", encoding="utf-8")

lines = words = chars = 0
longest = ""
with open(path, encoding="utf-8") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
        text = line.rstrip("\n")
        if len(text) > len(longest):
            longest = text

print(f"Lines: {lines}, words: {words}, characters: {chars}")
print("Longest line:", longest)