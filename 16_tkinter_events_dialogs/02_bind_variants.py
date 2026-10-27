import tkinter as tk

root = tk.Tk()
root.title("bind variants")
root.geometry("460x560")

log = tk.Text(root, height=9, state="disabled", bg="#f6f6f6")
log.pack(side="bottom", fill="x", padx=8, pady=8)

def say(message):
    log.config(state="normal")             # a disabled Text ignores insert()
    log.insert(tk.END, message + "\n")
    log.see(tk.END)
    log.config(state="disabled")

def clear_log(event=None):
    log.config(state="normal")
    log.delete("1.0", tk.END)
    log.config(state="disabled")

# 1. Hover effect with <Enter> and <Leave>
hover = tk.Button(root, text="Hover over me", width=24)
hover.pack(pady=6)
hover.bind("<Enter>", lambda e: hover.config(bg="gold", text="Pointer is over me"))
hover.bind("<Leave>", lambda e: hover.config(bg=root.cget("bg"), text="Hover over me"))

# 2. Keys inside an Entry. The MOST SPECIFIC matching binding wins on one widget
entry = tk.Entry(root, width=34)
entry.pack(pady=6)
entry.bind("<Return>", lambda e: say(f"Return pressed, text = {entry.get()!r}"))
entry.bind("<Escape>", lambda e: entry.delete(0, tk.END))
entry.bind("<FocusIn>", lambda e: say("entry gained focus"))
entry.bind("<FocusOut>", lambda e: say("entry lost focus"))

def block_x(event):
    if event.char.lower() == "x":
        say("x blocked by returning 'break'")
        return "break"                    # stops Tk's own class binding from inserting the character

entry.bind("<Key>", block_x)
print("bindtags:", entry.bindtags())      # widget, class, toplevel, all: the order callbacks run in

# 3. A Listbox: a virtual event and a double-click
box = tk.Listbox(root, height=4, exportselection=False)
for item in ("Python", "SQL", "Git", "Docker"):
    box.insert(tk.END, item)
box.pack(pady=6)
box.bind("<<ListboxSelect>>",
         lambda e: say(f"selected: {[box.get(i) for i in box.curselection()]}"))
box.bind("<Double-Button-1>", lambda e: say(f"double-clicked: {box.get(box.nearest(e.y))}"))

# 4. <Configure> fires for every widget, so check which one it was
size = tk.Label(root, text="")
size.pack()

def on_resize(event):
    if event.widget is root:
        size.config(text=f"window is {event.width} x {event.height}")

root.bind("<Configure>", on_resize)

# 5. command and bind on the same button: which runs first?
both = tk.Button(root, text="bind and command",
                 command=lambda: say("command ran (on mouse RELEASE)"))
both.bind("<Button-1>", lambda e: say("bind ran (on mouse PRESS)"))
both.pack(pady=6)

# 6. Turning a binding on and off
enabled = tk.BooleanVar(value=False)
target = tk.Label(root, text="Click me while the binding is ON", bg="lightblue", padx=10, pady=4)
target.pack(pady=4)

def toggle():
    if enabled.get():
        target.bind("<Button-1>", lambda e: say("target clicked"))
    else:
        target.unbind("<Button-1>")

tk.Checkbutton(root, text="binding on", variable=enabled, command=toggle).pack()

# 7. Shortcuts: bind on one window versus bind_all
root.bind("<Control-l>", clear_log)
root.bind_all("<F1>", lambda e: say("F1 pressed (bind_all works from any widget)"))

root.mainloop()