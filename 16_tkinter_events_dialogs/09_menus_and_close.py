import tkinter as tk
from tkinter import messagebox

def shortcut(func):
    """Turn a function into a key binding that also stops Tk's default behaviour."""
    def handler(event):
        func()
        return "break"
    return handler

root = tk.Tk()
root.title("Menus")
root.geometry("520x360")

status = tk.Label(root, text="Ready", anchor="w", relief="sunken")
status.pack(side="bottom", fill="x")
text = tk.Text(root, wrap="word", undo=True, font=("Consolas", 11))
text.pack(fill="both", expand=True)
text.focus()

wrap = tk.BooleanVar(value=True)
font_size = tk.IntVar(value=11)
show_status = tk.BooleanVar(value=True)

def say(message):
    status.config(text=message)

def new_doc():
    text.delete("1.0", tk.END)
    say("New document")

def undo():
    try:
        text.edit_undo()
    except tk.TclError:                         # raised when there is nothing to undo
        say("Nothing to undo")

def apply_wrap():
    text.config(wrap="word" if wrap.get() else "none")

def apply_font():
    text.config(font=("Consolas", font_size.get()))

def toggle_status():
    if show_status.get():
        status.pack(side="bottom", fill="x")
    else:
        status.pack_forget()

def about():
    messagebox.showinfo("About", "Menu demo\nTkinter, Day 17", parent=root)

def exit_app():
    if text.get("1.0", "end-1c").strip():
        if not messagebox.askokcancel("Quit", "Quit and lose the text?", parent=root):
            return
    root.destroy()

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", command=new_doc)
file_menu.add_command(label="Save (disabled)", state="disabled")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

edit_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=edit_menu, underline=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text.event_generate("<<Paste>>"))

view_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="View", menu=view_menu, underline=0)
view_menu.add_checkbutton(label="Word wrap", variable=wrap, command=apply_wrap)
view_menu.add_checkbutton(label="Status bar", variable=show_status, command=toggle_status)
size_menu = tk.Menu(view_menu, tearoff=False)
view_menu.add_cascade(label="Font size", menu=size_menu)
for points in (9, 11, 14, 18):
    size_menu.add_radiobutton(label=f"{points} pt", variable=font_size, value=points, command=apply_font)

help_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=help_menu, underline=0)
help_menu.add_command(label="About", command=about)

# A right-click (context) menu
context = tk.Menu(root, tearoff=False)
context.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
context.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
context.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))

def popup(event):
    try:
        context.tk_popup(event.x_root, event.y_root)
    finally:
        context.grab_release()

text.bind("<Button-3>", popup)

# accelerator= only DISPLAYS text. A shortcut needs a binding, and it must be on the Text widget
# so that "break" can stop Tk's own Ctrl+N ("next line") from also running
text.bind("<Control-n>", shortcut(new_doc))

root.protocol("WM_DELETE_WINDOW", exit_app)               # runs when the user clicks the window's X

root.mainloop()