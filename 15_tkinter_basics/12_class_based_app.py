import tkinter as tk

class CounterApp(tk.Tk):
    def __init__(self):
        super().__init__()                  # forget this and nothing works (Day 13)
        self.title("Counter (class-based)")
        self.geometry("300x220")
        self.count = tk.IntVar(value=0)     # created AFTER Tk() exists
        self._build()

    def _build(self):
        tk.Label(self, textvariable=self.count, font=("Arial", 32)).pack(pady=10)
        row = tk.Frame(self)
        row.pack()
        tk.Button(row, text="-", width=4, command=lambda: self.change(-1)).pack(side="left", padx=5)
        tk.Button(row, text="+", width=4, command=lambda: self.change(+1)).pack(side="left", padx=5)
        tk.Button(self, text="Reset", command=lambda: self.count.set(0)).pack(pady=8)
        tk.Button(self, text="About", command=self.open_about).pack()

    def change(self, delta):
        self.count.set(self.count.get() + delta)

    def open_about(self):
        win = tk.Toplevel(self)             # a second window that belongs to the first
        win.title("About")
        win.geometry("220x100")
        tk.Label(win, text="Counter app v1").pack(pady=10)
        tk.Button(win, text="Close", command=win.destroy).pack()

if __name__ == "__main__":
    CounterApp().mainloop()