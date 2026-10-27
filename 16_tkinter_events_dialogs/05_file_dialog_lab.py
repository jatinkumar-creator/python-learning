import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)
(SCRATCH / "sample.txt").write_text("Hello from sample.txt\nनमस्ते, café\n", encoding="utf-8")

FILETYPES = [("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]

root = tk.Tk()
root.title("File dialog lab")
root.geometry("560x460")

status = tk.Label(root, text="Ready", anchor="w", relief="sunken")
status.pack(side="bottom", fill="x")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=8, pady=8)
text = tk.Text(frame, wrap="word")
scroll = tk.Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

def open_file():
    path = filedialog.askopenfilename(parent=root, title="Open a text file",
                                      initialdir=str(SCRATCH), filetypes=FILETYPES)
    print("askopenfilename returned:", repr(path))
    if not path:                                       # '' means the user cancelled
        status.config(text="Open cancelled")
        return
    try:
        content = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        messagebox.showerror("Cannot open file", f"{type(e).__name__}: {e}", parent=root)
        return
    text.delete("1.0", tk.END)
    text.insert("1.0", content)
    status.config(text=f"Opened {Path(path).name} ({len(content)} characters)")

def save_file():
    path = filedialog.asksaveasfilename(parent=root, title="Save as", initialdir=str(SCRATCH),
                                        initialfile="notes.txt", defaultextension=".txt",
                                        filetypes=FILETYPES)
    print("asksaveasfilename returned:", repr(path))
    if not path:
        status.config(text="Save cancelled")
        return
    try:
        Path(path).write_text(text.get("1.0", "end-1c"), encoding="utf-8")
    except OSError as e:
        messagebox.showerror("Cannot save", f"{type(e).__name__}: {e}", parent=root)
        return
    status.config(text=f"Saved {Path(path).name}")

def open_many():
    paths = filedialog.askopenfilenames(parent=root, title="Pick several files",
                                        initialdir=str(SCRATCH), filetypes=FILETYPES)
    print("askopenfilenames returned:", repr(paths))
    if not paths:
        status.config(text="Nothing chosen")
        return
    status.config(text=f"{len(paths)} files: " + ", ".join(Path(p).name for p in paths))

def choose_folder():
    folder = filedialog.askdirectory(parent=root, title="Pick a folder", initialdir=str(SCRATCH))
    print("askdirectory returned:", repr(folder))
    if not folder:
        status.config(text="No folder chosen")
        return
    names = sorted(p.name for p in Path(folder).glob("*.txt"))
    text.delete("1.0", tk.END)
    text.insert("1.0", f"{folder}\n\n" + ("\n".join(names) or "(no .txt files)"))
    status.config(text=f"{len(names)} text files found")

bar = tk.Frame(root)
bar.pack(side="bottom", fill="x", padx=8)
for label, command in (("Open...", open_file), ("Save as...", save_file),
                       ("Open several...", open_many), ("Pick folder...", choose_folder)):
    tk.Button(bar, text=label, command=command).pack(side="left", padx=2, pady=4)

root.mainloop()