import tkinter as tk

root = tk.Tk()
root.title("My first window")

# Centre a 400x200 window on the screen
w, h = 400, 200
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")         # "widthxheight+x+y"
root.resizable(True, False)               # width resizable, height fixed
root.minsize(300, 150)

print(type(root).__name__, root.winfo_class())
print("Tk version:", tk.TkVersion)
print("Screen:", root.winfo_screenwidth(), "x", root.winfo_screenheight())

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=40)

print("before mainloop")
root.mainloop()                           # blocks here until you close the window
print("after mainloop: the window was closed")