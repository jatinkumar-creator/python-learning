import tkinter as tk

root = tk.Tk()
root.title("Greeter")
root.geometry("360x240")

tk.Label(root, text="Your name:").pack(pady=(15, 0))
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.insert(0, "type here")
entry.select_range(0, tk.END)
entry.focus()                            # the cursor starts in this box

result = tk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)

def greet():
    name = entry.get().strip()           # get() always returns a str
    if name:
        result.config(text=f"Hello, {name}!", fg="black")
    else:
        result.config(text="Please type a name.", fg="red")

def clear():
    entry.delete(0, tk.END)              # from character 0 to the end
    result.config(text="")
    entry.focus()

tk.Button(root, text="Greet", command=greet).pack(pady=2)
tk.Button(root, text="Clear", command=clear).pack(pady=2)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=2)

root.mainloop()