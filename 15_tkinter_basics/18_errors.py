# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="a").pack()
# tk.Label(root, text="b").grid(row=0, column=0)    # TclError: cannot use geometry manager grid inside . which already has slaves managed by pack
# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, txt="oops").pack()                 # TclError: unknown option "-txt"

# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="x", bg="notacolor").pack()   # TclError: unknown color name

# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="x").pack(side="middle")      # TclError: bad side

# import tkinter as tk
# var = tk.StringVar()                              # RuntimeError: Too early to create variable (no Tk() yet)

# import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="x")
# label.pack()
# root.destroy()
# label.config(text="y")                            # TclError: invalid command name (the widget is gone)

# import tkinter as tk
# root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()
# entry.insert(0, "5")
# print(entry.get() + 1)                            # TypeError: get() returns a string

# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="I am invisible")             # no pack/grid/place: the label never appears
# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# tk.Label(root, text="forgot mainloop").pack()     # the window opens and closes instantly