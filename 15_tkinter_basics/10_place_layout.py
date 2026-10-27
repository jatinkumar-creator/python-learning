import tkinter as tk

root = tk.Tk()
root.title("place")
root.geometry("420x300")

tk.Label(root, text="x=20, y=20 (absolute)", bg="gold").place(x=20, y=20)
tk.Label(root, text="centre of the window", bg="skyblue").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(root, text="bottom right", bg="lightgreen").place(relx=1.0, rely=1.0, anchor="se")
tk.Label(root, text="width = half the window", bg="violet").place(relx=0, rely=0.8, relwidth=0.5)

root.mainloop()