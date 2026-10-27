import tkinter as tk

root = tk.Tk()
root.title("grid")

# A form
form = tk.LabelFrame(root, text="Sign-up form", padx=10, pady=10)
form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(form, text="Name").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Entry(form).grid(row=0, column=1, sticky="ew", padx=5, pady=5)
tk.Label(form, text="Email").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Entry(form).grid(row=1, column=1, sticky="ew", padx=5, pady=5)
tk.Label(form, text="Notes").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
tk.Text(form, width=30, height=4).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Checkbutton(form, text="Subscribe to the newsletter").grid(row=3, column=1, sticky="w")
tk.Button(form, text="Submit").grid(row=4, column=0, columnspan=2, pady=10)     # spans both columns

# A keypad built with loops
pad = tk.LabelFrame(root, text="Keypad", padx=10, pady=10)
pad.grid(row=1, column=0, padx=10, pady=(0, 10))
keys = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["0", ".", "="]]
for r, row in enumerate(keys):
    for c, key in enumerate(row):
        tk.Button(pad, text=key, width=4, height=2).grid(row=r, column=c, padx=2, pady=2)

# Which rows and columns absorb extra space when the window grows?
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
form.columnconfigure(1, weight=1)
form.rowconfigure(2, weight=1)

root.mainloop()