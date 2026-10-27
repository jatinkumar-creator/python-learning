import tkinter as tk

root = tk.Tk()
root.title("Entry features")
root.geometry("380x420")

# 1. A password field
tk.Label(root, text="Password:").pack()
pwd = tk.Entry(root, show="*")
pwd.pack()

# 2. A StringVar linked to an Entry, with a live preview
name_var = tk.StringVar()
tk.Label(root, text="Type here:").pack(pady=(10, 0))
tk.Entry(root, textvariable=name_var).pack()
live = tk.Label(root, text="")
live.pack()
name_var.trace_add("write", lambda *args: live.config(text=f"You typed: {name_var.get()}"))

# 3. A read-only Entry
ro = tk.Entry(root)
ro.insert(0, "read only text")
ro.config(state="readonly")
ro.pack(pady=10)

# 4. Validation: digits only
def only_digits(proposed):
    return proposed == "" or proposed.isdigit()

vcmd = (root.register(only_digits), "%P")          # %P = the text as it WOULD be after the keystroke
tk.Label(root, text="Digits only:").pack()
tk.Entry(root, validate="key", validatecommand=vcmd).pack()

# 5. Reading a number safely (get() returns text, just like input())
tk.Label(root, text="Your age:").pack(pady=(10, 0))
age_entry = tk.Entry(root)
age_entry.pack()
out = tk.Label(root, text="")
out.pack()

def next_year():
    text = age_entry.get()
    try:
        out.config(text=f"Next year you will be {int(text) + 1}", fg="black")
    except ValueError:
        out.config(text=f"{text!r} is not a whole number", fg="red")

tk.Button(root, text="Calculate", command=next_year).pack(pady=5)

root.mainloop()