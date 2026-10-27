from pathlib import Path

with open("cwd_demo.txt", "w", encoding="utf-8") as f:
    f.write("x")
print("Created:", Path("cwd_demo.txt").resolve())