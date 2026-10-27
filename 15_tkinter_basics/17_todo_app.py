import tkinter as tk

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-do list")
        self.geometry("360x380")
        self.tasks = []

        top = tk.Frame(self, padx=10, pady=10)
        top.pack(fill="x")
        self.entry = tk.Entry(top)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.focus()
        tk.Button(top, text="Add", command=self.add_task).pack(side="left", padx=(5, 0))

        middle = tk.Frame(self, padx=10)
        middle.pack(fill="both", expand=True)
        self.listbox = tk.Listbox(middle, selectmode="single")
        scroll = tk.Scrollbar(middle, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True)

        bottom = tk.Frame(self, padx=10, pady=10)
        bottom.pack(fill="x")
        tk.Button(bottom, text="Delete selected", command=self.delete_task).pack(side="left")
        tk.Button(bottom, text="Clear all", command=self.clear_all).pack(side="left", padx=5)

        self.status = tk.Label(self, text="0 tasks", anchor="w", padx=10)
        self.status.pack(fill="x")

    def refresh_status(self):
        n = len(self.tasks)
        self.status.config(text=f"{n} task{'s' if n != 1 else ''}", fg="black")

    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            self.status.config(text="Type a task first", fg="red")
            return
        self.tasks.append(title)
        self.listbox.insert(tk.END, title)
        self.entry.delete(0, tk.END)
        self.refresh_status()

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            self.status.config(text="Select a task first", fg="red")
            return
        index = selection[0]
        self.listbox.delete(index)
        del self.tasks[index]
        self.refresh_status()

    def clear_all(self):
        self.listbox.delete(0, tk.END)
        self.tasks.clear()
        self.refresh_status()

if __name__ == "__main__":
    TodoApp().mainloop()