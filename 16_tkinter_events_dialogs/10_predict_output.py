import tkinter as tk

root = tk.Tk()
root.withdraw()

frame = tk.Frame(root)

# 1
log = []
frame.bind("<<Ping>>", lambda e: log.append("frame"))
root.bind("<<Ping>>", lambda e: log.append("root"))
frame.event_generate("<<Ping>>")
print(log)

# 2
log = []

def stop(event):
    log.append("frame")
    return "break"

frame.bind("<<Stop>>", stop)
root.bind("<<Stop>>", lambda e: log.append("root"))
frame.event_generate("<<Stop>>")
print(log)

# 3
log = []
frame.bind("<<Order>>", lambda e: log.append("widget"))
root.bind("<<Order>>", lambda e: log.append("toplevel"))
root.bind_all("<<Order>>", lambda e: log.append("all"))
frame.event_generate("<<Order>>")
print(log)

# 4
seen = []
v = tk.IntVar(value=1)
v.trace_add("write", lambda *args: seen.append(v.get()))
v.set(5)
v.set(7)
v.set(7)
print(seen)

# 5
button = tk.Button(root, text="x", command=lambda: "hi")
print(button.invoke())

# 6
canvas = tk.Canvas(root)
a = canvas.create_rectangle(0, 0, 10, 10)
b = canvas.create_oval(5, 5, 15, 15)
print(a, b, canvas.find_all())
canvas.move(a, 5, 5)
print(canvas.coords(a))
canvas.delete(a)
c = canvas.create_line(0, 0, 1, 1)
print(c, canvas.find_all(), canvas.type(b), repr(canvas.itemcget(b, "fill")))

# 7
image = tk.PhotoImage(width=4, height=2)
big = image.zoom(3)
small = big.subsample(2)
print((image.width(), image.height()), (big.width(), big.height()), (small.width(), small.height()))

# 8
print(frame.bind("<<Q>>") == "")
frame.bind("<<Q>>", lambda e: None)
print(frame.bind("<<Q>>") == "")
frame.unbind("<<Q>>")
print(frame.bind("<<Q>>") == "")

# 9
who = []
frame.bind("<<Who>>", lambda e: who.append((e.widget is frame, type(e.widget).__name__)))
frame.event_generate("<<Who>>")
print(who)

# 10
sv = tk.StringVar()
entry = tk.Entry(root, textvariable=sv)
sv.set("abc")
print(entry.get())
entry.insert(tk.END, "d")
print(sv.get())

# 11
box = tk.Listbox(root)
box.insert(tk.END, "a", "b", "c")
box.selection_set(1)
print(box.size(), box.curselection(), box.get(1), box.get(0, tk.END))

# 12
timer = root.after(100000, lambda: None)
print(type(timer).__name__)
root.after_cancel(timer)

# 13
top = tk.Toplevel(root)
top.withdraw()
print(top.winfo_class(), repr(top.winfo_parent()), repr(root.winfo_parent()), top in root.winfo_children())

root.destroy()