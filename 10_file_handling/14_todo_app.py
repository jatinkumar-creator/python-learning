import json
from common import SCRATCH

FILE = SCRATCH / "todo.json"

def load():
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("The file was damaged, starting with an empty list.")
        return []

def save(tasks):
    tmp = FILE.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:       # write a temporary copy first...
        json.dump(tasks, f, indent=2)
    tmp.replace(FILE)                                 # ...then swap it in, so a crash can't leave half a file

def show(tasks):
    if not tasks:
        print("  (no tasks)")
    for i, t in enumerate(tasks, start=1):
        print(f"  {i}. [{'x' if t['done'] else ' '}] {t['title']}")

tasks = load()
while True:
    print("\n1. Add  2. List  3. Mark done  4. Delete  5. Quit")
    choice = input("Choice: ").strip()
    if choice == "1":
        title = input("Task: ").strip()
        if title:
            tasks.append({"title": title, "done": False})
            save(tasks)
    elif choice == "2":
        show(tasks)
    elif choice in ("3", "4"):
        show(tasks)
        try:
            index = int(input("Number: ")) - 1
            if choice == "3":
                tasks[index]["done"] = True
            else:
                tasks.pop(index)
            save(tasks)
        except (ValueError, IndexError):
            print("Invalid number.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")