import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog

FILETYPES = [("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]

def shortcut(func):
    def handler(event):
        func()
        return "break"                        # stops Tk's own binding for the same keys
    return handler

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x440")
        self.path = None
        self.wrap = tk.BooleanVar(value=True)
        self.font_size = tk.IntVar(value=11)
        self._build_widgets()
        self._build_menu()
        self._bind_keys()
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.refresh_title()
        self.refresh_status()

    # ----- building the window -----
    def _build_widgets(self):
        self.status = tk.Label(self, text="", anchor="w", relief="sunken", padx=6)
        self.status.pack(side="bottom", fill="x")
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        self.text = tk.Text(frame, wrap="word", undo=True, font=("Consolas", 11))
        scroll = tk.Scrollbar(frame, command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.tag_configure("found", background="yellow")
        self.text.focus()

    def _build_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        edit_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Edit", menu=edit_menu, underline=0)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X",
                              command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C",
                              command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V",
                              command=lambda: self.text.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Select all", accelerator="Ctrl+A", command=self.select_all)
        edit_menu.add_command(label="Find...", accelerator="Ctrl+F", command=self.find)

        view_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="View", menu=view_menu, underline=0)
        view_menu.add_checkbutton(label="Word wrap", variable=self.wrap, command=self.apply_wrap)
        size_menu = tk.Menu(view_menu, tearoff=False)
        view_menu.add_cascade(label="Font size", menu=size_menu)
        for points in (9, 11, 14, 18):
            size_menu.add_radiobutton(label=f"{points} pt", variable=self.font_size,
                                      value=points, command=self.apply_font)

        help_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help", menu=help_menu, underline=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
            "About", "Notepad built with Tkinter", parent=self))

    def _bind_keys(self):
        t = self.text
        t.bind("<Control-n>", shortcut(self.new_file))
        t.bind("<Control-o>", shortcut(self.open_file))
        t.bind("<Control-s>", shortcut(self.save))
        t.bind("<Control-Shift-S>", shortcut(self.save_as))
        t.bind("<Control-a>", shortcut(self.select_all))
        t.bind("<Control-f>", shortcut(self.find))
        t.bind("<<Modified>>", lambda e: self.refresh_title())
        for sequence in ("<KeyRelease>", "<ButtonRelease-1>"):
            t.bind(sequence, lambda e: self.refresh_status())

    # ----- keeping the title and status bar up to date -----
    def refresh_title(self):
        name = self.path.name if self.path else "Untitled"
        star = "*" if self.text.edit_modified() else ""
        self.title(f"{star}{name} - Notepad")

    def refresh_status(self):
        line, col = self.text.index("insert").split(".")
        characters = len(self.text.get("1.0", "end-1c"))
        self.status.config(text=f"Ln {line}, Col {int(col) + 1}   |   {characters} characters")

    # ----- file operations -----
    def confirm_discard(self):
        """True when it is safe to throw the current text away."""
        if not self.text.edit_modified():
            return True
        name = self.path.name if self.path else "Untitled"
        answer = messagebox.askyesnocancel("Unsaved changes", f"Save changes to {name}?", parent=self)
        if answer is None:                       # Cancel
            return False
        if answer:                               # Yes: save first, and only continue if that worked
            return self.save()
        return True                              # No: discard

    def _replace_text(self, content):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self.text.edit_reset()                   # forget the undo history
        self.text.edit_modified(False)
        self.refresh_status()

    def new_file(self):
        if self.confirm_discard():
            self.path = None
            self._replace_text("")
            self.refresh_title()

    def open_file(self):
        if not self.confirm_discard():
            return
        path = filedialog.askopenfilename(parent=self, filetypes=FILETYPES)
        if not path:
            return
        try:
            content = Path(path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            messagebox.showerror("Cannot open file", f"{type(e).__name__}: {e}", parent=self)
            return
        self.path = Path(path)
        self._replace_text(content)
        self.refresh_title()

    def save(self):
        if self.path is None:
            return self.save_as()
        return self._write(self.path)

    def save_as(self):
        path = filedialog.asksaveasfilename(parent=self, defaultextension=".txt",
                                            filetypes=FILETYPES,
                                            initialfile=self.path.name if self.path else "untitled.txt")
        if not path:
            return False
        if self._write(Path(path)):
            self.path = Path(path)
            self.refresh_title()
            return True
        return False

    def _write(self, path):
        try:
            path.write_text(self.text.get("1.0", "end-1c"), encoding="utf-8")
        except OSError as e:
            messagebox.showerror("Cannot save file", f"{type(e).__name__}: {e}", parent=self)
            return False
        self.text.edit_modified(False)
        self.refresh_title()
        return True

    def exit_app(self):
        if self.confirm_discard():
            self.destroy()

    # ----- editing helpers -----
    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass                                 # nothing to undo

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end-1c")
        self.text.mark_set("insert", "end-1c")

    def find(self):
        term = simpledialog.askstring("Find", "Find text:", parent=self)
        self.text.tag_remove("found", "1.0", tk.END)
        if not term:
            return
        start, first, count = "1.0", None, 0
        while True:
            index = self.text.search(term, start, stopindex=tk.END, nocase=True)
            if not index:
                break
            end = f"{index}+{len(term)}c"
            self.text.tag_add("found", index, end)
            first = first or index
            start = end
            count += 1
        if first:
            self.text.see(first)
        self.status.config(text=f"{count} match{'es' if count != 1 else ''} for {term!r}")

    def apply_wrap(self):
        self.text.config(wrap="word" if self.wrap.get() else "none")

    def apply_font(self):
        self.text.config(font=("Consolas", self.font_size.get()))

if __name__ == "__main__":
    Notepad().mainloop()