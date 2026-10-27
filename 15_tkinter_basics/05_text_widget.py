import tkinter as tk

root = tk.Tk()
root.title("Text widget")
root.geometry("480x400")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

text = tk.Text(frame, wrap="word", height=10, width=50)
scroll = tk.Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scroll.set)           # connect both directions
scroll.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

# Text indexes are "line.column": line 1 is "1.0", the end is tk.END
text.insert("1.0", "First line\nSecond line\n")
text.insert(tk.END, "Appended at the end\n")
text.insert("2.0", ">> inserted before line 2\n")

text.tag_configure("title", font=("Arial", 12, "bold"), foreground="darkblue")
text.tag_add("title", "1.0", "1.end")             # style the whole first line

print(repr(text.get("1.0", tk.END)))              # note the extra "\n" Tk adds at the end
print(repr(text.get("1.0", "end-1c")))            # "end-1c" means one character before the end
print(text.get("2.0", "2.end"))
print(text.index(tk.END), text.index("end-1c"))

status = tk.Label(root, text="", anchor="w")
status.pack(fill="x", padx=10)

def count():
    content = text.get("1.0", "end-1c")
    status.config(text=f"{len(content.split())} words, {len(content)} characters, "
                       f"{content.count(chr(10)) + 1} lines")

def clear():
    text.delete("1.0", tk.END)
    status.config(text="Cleared")

tk.Button(root, text="Count", command=count).pack(side="left", padx=10, pady=5)
tk.Button(root, text="Clear", command=clear).pack(side="left")

root.mainloop()