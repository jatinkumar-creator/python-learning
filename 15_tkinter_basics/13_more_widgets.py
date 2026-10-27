import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("More widgets")
root.geometry("340x460")

agree = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="I agree to the terms", variable=agree).pack(anchor="w", padx=10, pady=(10, 0))

level = tk.StringVar(value="beginner")
for value in ("beginner", "intermediate", "expert"):
    tk.Radiobutton(root, text=value.title(), variable=level, value=value).pack(anchor="w", padx=10)

tk.Label(root, text="Skills:").pack(anchor="w", padx=10, pady=(10, 0))
skills = tk.Listbox(root, height=4, selectmode="extended", exportselection=False)
for item in ("Python", "SQL", "Git", "Docker"):
    skills.insert(tk.END, item)
skills.pack(anchor="w", padx=10)

volume = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Volume")
volume.set(30)
volume.pack(fill="x", padx=10)

city = ttk.Combobox(root, values=["Delhi", "Pune", "Mumbai"], state="readonly")
city.set("Delhi")
city.pack(anchor="w", padx=10, pady=5)

output = tk.Label(root, justify="left", anchor="w")
output.pack(fill="x", padx=10, pady=5)

def show():
    picked = [skills.get(i) for i in skills.curselection()]
    output.config(text=f"agree = {agree.get()}\nlevel = {level.get()}\nskills = {picked}\n"
                       f"volume = {volume.get()}\ncity = {city.get()}")

tk.Button(root, text="Show values", command=show).pack(pady=5)
root.mainloop()