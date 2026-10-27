# import tkinter as tk
# root = tk.Tk()
# tk.messagebox.showinfo("Hi", "x")           # AttributeError (unless something else imported tkinter.messagebox)

# import tkinter as tk
# root = tk.Tk()
# b = tk.Button(root, text="click me")
# b.pack()
# b.bind("<Button-1>", lambda: print("clicked"))      # click it: TypeError, because the callback must accept the event
# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# tk.Button(root, text="b", command=lambda event: print(event)).pack()   # click: TypeError, command passes no argument
# root.mainloop()

# import tkinter as tk
# tk.PhotoImage(file="missing.png")                    # TclError: couldn't open ... no such file or directory

# import tkinter as tk
# from pathlib import Path
# fake = Path(__file__).resolve().parent / "scratch" / "fake.png"
# fake.parent.mkdir(exist_ok=True)
# fake.write_text("not an image")
# root = tk.Tk()
# tk.PhotoImage(file=str(fake))                        # TclError: couldn't recognize data in image file

# import tkinter as tk
# root = tk.Tk()
# root.bind("<Keypress-bogus>", print)                 # TclError: bad event type or keysym "bogus"

# import tkinter as tk
# root = tk.Tk()
# canvas = tk.Canvas(root)
# canvas.create_rectangle(1, 2, 3)                     # TclError: wrong number of coordinates

# import tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# path = filedialog.askopenfilename()
# open(path)                                           # press Cancel: FileNotFoundError ... ''

# import tkinter as tk
# from tkinter import simpledialog
# root = tk.Tk()
# age = simpledialog.askinteger("Age", "Your age?")
# print(age + 1)                                       # press Cancel: TypeError, because None + 1












# 1. Key events on a Frame that has no focus: nothing happens
# import tkinter as tk
# root = tk.Tk()
# frame = tk.Frame(root, width=200, height=100, bg="gray")
# frame.pack()
# frame.bind("<Key>", lambda e: print(e.keysym))       # type: nothing prints. Add frame.focus_set() and try again
# root.mainloop()

# 2. A local PhotoImage: the label shows no picture (see Exercise 6, "Show broken")