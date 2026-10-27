import os
from pathlib import Path

root = Path(__file__).resolve().parents[1]            # the project root
SKIP = {"venv", ".git", "__pycache__", "scratch"}

term = input("Search for: ").strip()
if not term:
    raise SystemExit("Nothing to search for.")

hits = 0
for folder, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in SKIP]      # prune: never walk into venv
    for name in files:
        if not name.endswith(".py"):
            continue
        path = Path(folder) / name
        try:
            with open(path, encoding="utf-8") as f:
                for number, line in enumerate(f, start=1):
                    if term.lower() in line.lower():
                        print(f"{path.relative_to(root)}:{number}: {line.strip()}")
                        hits += 1
        except (UnicodeDecodeError, PermissionError) as e:
            print("skipped", path, "-", type(e).__name__)

print(f"{hits} matches")