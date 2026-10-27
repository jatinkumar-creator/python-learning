import tkinter as tk

root = tk.Tk()
root.title("Frames")
root.geometry("460x320")

# Header
header = tk.Frame(root, bg="steelblue", height=50)
header.pack(fill="x")
header.pack_propagate(False)               # keep height=50 instead of shrinking to the label
tk.Label(header, text="Header", bg="steelblue", fg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

# Footer
footer = tk.Frame(root, bg="gray20", height=25)
footer.pack(fill="x", side="bottom")

# Body: a sidebar and a content area side by side
body = tk.Frame(root)
body.pack(fill="both", expand=True)

sidebar = tk.Frame(body, bg="lightgray", width=110)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)
tk.Label(sidebar, text="Menu", bg="lightgray").pack(pady=5)
for item in ("Home", "Profile", "Settings"):
    tk.Button(sidebar, text=item).pack(fill="x", padx=5, pady=2)

content = tk.Frame(body, padx=10, pady=10)
content.pack(side="left", fill="both", expand=True)

# A LabelFrame draws a titled border. It uses grid INSIDE, while its parent uses pack
form = tk.LabelFrame(content, text="Contact", padx=10, pady=10)
form.pack(fill="x")
tk.Label(form, text="Name").grid(row=0, column=0, sticky="w")
tk.Entry(form).grid(row=0, column=1, padx=5, pady=2)
tk.Label(form, text="Email").grid(row=1, column=0, sticky="w")
tk.Entry(form).grid(row=1, column=1, padx=5, pady=2)

print([type(w).__name__ for w in root.winfo_children()])
print([type(w).__name__ for w in body.winfo_children()])
print(form.winfo_parent(), form.winfo_class())

root.mainloop()