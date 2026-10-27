import tkinter as tk
from tkinter import colorchooser, messagebox, simpledialog

root = tk.Tk()
root.title("Dialog lab")
root.geometry("420x560")

out = tk.Label(root, text="returned: (nothing yet)", font=("Consolas", 10),
               wraplength=400, justify="left")
out.pack(side="bottom", fill="x", padx=8, pady=8)

def run(name, action):
    print(f"{name}: dialog opening, the code below waits...")
    result = action()
    print(f"{name}: dialog closed")
    text = f"{name}\n  returned: {result!r}  (type {type(result).__name__})"
    out.config(text=text)
    print(text)

ACTIONS = [
    ("showinfo",       lambda: messagebox.showinfo("Information", "File saved successfully", parent=root)),
    ("showwarning",    lambda: messagebox.showwarning("Warning", "Disk space is low", parent=root)),
    ("showerror",      lambda: messagebox.showerror("Error", "Could not open the file", parent=root)),
    ("askquestion",    lambda: messagebox.askquestion("Question", "Do you like Python?", parent=root)),
    ("askokcancel",    lambda: messagebox.askokcancel("Confirm", "Continue with this action?", parent=root)),
    ("askyesno",       lambda: messagebox.askyesno("Delete", "Delete this file?", icon="warning", parent=root)),
    ("askyesnocancel", lambda: messagebox.askyesnocancel("Unsaved changes", "Save before closing?", parent=root)),
    ("askretrycancel", lambda: messagebox.askretrycancel("Network", "Connection failed. Try again?", parent=root)),
    ("askstring",      lambda: simpledialog.askstring("Name", "Your name?", parent=root)),
    ("askinteger",     lambda: simpledialog.askinteger("Age", "Your age?", minvalue=0, maxvalue=120, parent=root)),
    ("askfloat",       lambda: simpledialog.askfloat("Price", "Price?", minvalue=0, parent=root)),
    ("askcolor",       lambda: colorchooser.askcolor(title="Pick a colour", parent=root)),
]

for name, action in ACTIONS:
    tk.Button(root, text=name, width=18,
              command=lambda n=name, a=action: run(n, a)).pack(pady=2)     # n=name, a=action: the loop-trap fix

root.mainloop()