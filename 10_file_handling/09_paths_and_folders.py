import os
import shutil
from pathlib import Path
from common import SCRATCH

d = SCRATCH / "demo_dir"
d.mkdir(exist_ok=True)
(d / "a.txt").write_text("A", encoding="utf-8")
(d / "b.txt").write_text("BB", encoding="utf-8")
(d / "sub").mkdir(exist_ok=True)
(d / "sub" / "c.log").write_text("CCC", encoding="utf-8")

print(d.exists(), d.is_dir(), (d / "a.txt").is_file())
print(sorted(p.name for p in d.iterdir()))
print(sorted(p.name for p in d.glob("*.txt")))
print(sorted(str(p.relative_to(d)) for p in d.rglob("*")))
print((d / "b.txt").stat().st_size, "bytes")
print(sorted(os.listdir(d)))

# Rename, copy, delete
(d / "a.txt").rename(d / "a_renamed.txt")
shutil.copy(d / "b.txt", d / "b_copy.txt")
(d / "b.txt").unlink()
print(sorted(p.name for p in d.iterdir()))
shutil.rmtree(d)
print("after rmtree:", d.exists())

# Taking paths apart
p = Path("D:/AI_ENGINEERING/python-learning/notes.md")
print(p.name, p.stem, p.suffix, p.parent)
print(p.parts)
print(os.path.join("a", "b"), os.path.splitext("report.final.txt"))
print(Path("a") / "b" / "c.txt")

# Where am I, versus where is this script?
print("current folder:", os.getcwd())
print("script folder :", Path(__file__).resolve().parent)

# Windows path traps
print("C:\new\table.txt")                # \n and \t become characters!
print(r"C:\new\table.txt")               # a raw string keeps the backslashes
print(Path("C:/new/table.txt"))          # forward slashes work on Windows too