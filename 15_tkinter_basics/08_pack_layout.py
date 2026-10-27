import tkinter as tk

root = tk.Tk()
root.title("pack")
root.geometry("440x340")

tk.Label(root, text="1. top (default)", bg="tomato").pack()
tk.Label(root, text="2. fill x", bg="orange").pack(fill="x")
tk.Label(root, text="3. anchor w + padding", bg="khaki").pack(anchor="w", padx=20, pady=3)
tk.Label(root, text="4. side left, fill y", bg="gold").pack(side="left", fill="y")
tk.Label(root, text="5. side right, fill y", bg="lightgreen").pack(side="right", fill="y")
tk.Label(root, text="6. fill both + expand", bg="skyblue").pack(fill="both", expand=True, padx=10, pady=10)
tk.Label(root, text="7. bottom", bg="violet").pack(side="bottom", fill="x")

root.mainloop()