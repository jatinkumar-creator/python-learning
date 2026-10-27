import tkinter as tk

root = tk.Tk()
root.withdraw()                              # hide the window: we only inspect values

# 1
e = tk.Entry(root)
e.insert(0, "hello")
e.insert(tk.END, " world")
e.insert(0, ">> ")
print(repr(e.get()))

# 2
e.delete(0, 3)
print(repr(e.get()))

# 3
e.delete(0, tk.END)
print(repr(e.get()), type(e.get()).__name__)

# 4
v = tk.IntVar(value=5)
v.set(v.get() + 1)
print(v.get(), type(v.get()).__name__)

# 5
s = tk.StringVar(value="42")
print(s.get() + "1", int(s.get()) + 1)

# 6
b = tk.BooleanVar()
print(b.get())
b.set(True)
print(b.get())

# 7
lbl = tk.Label(root, text="A")
lbl.config(text="B")
lbl["text"] = "C"
print(lbl.cget("text"), lbl["text"])

# 8
t = tk.Text(root)
t.insert("1.0", "line1\nline2")
print(repr(t.get("1.0", tk.END)))
print(repr(t.get("1.0", "end-1c")))
print(t.get("2.0", "2.end"))

# 9
print([w.winfo_class() for w in root.winfo_children()])

# 10
def hello():
    return "hi"

btn = tk.Button(root, text="x", command=hello)
print(btn.invoke())

# 11
btn3 = tk.Button(root, text="z", state="disabled")
print(btn3["state"])
btn3.config(state="normal")
print(btn3["state"])

# 12
f = tk.Frame(root)
tk.Label(f, text="inside").pack()
tk.Label(f, text="also inside").pack()
print(len(f.winfo_children()))

# 13
x = tk.Label(root, text="trap").pack()
print(x)

# 14
try:
    tk.Label(root, txt="x")
except tk.TclError as err:
    print("TclError:", err)

# 15
try:
    tk.Label(root, bg="notacolor")
except tk.TclError as err:
    print("TclError:", err)

root.destroy()