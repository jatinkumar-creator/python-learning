import queue
import threading
import time
import tkinter as tk
from tkinter import ttk

STEPS = 100

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Threads + Tkinter")
        self.geometry("460x330")
        self.messages = queue.Queue()
        self.cancel_flag = threading.Event()
        self.worker = None
        self._build()
        self.tick_clock()
        self.poll()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _build(self):
        self.clock = tk.Label(self, font=("Consolas", 16))
        self.clock.pack(pady=8)
        self.status = tk.Label(self, text="Idle")
        self.status.pack()
        self.bar = ttk.Progressbar(self, maximum=STEPS, length=380)
        self.bar.pack(pady=8)

        row = tk.Frame(self)
        row.pack()
        self.start_btn = tk.Button(row, text="Start work (thread)", command=self.start_work)
        self.start_btn.pack(side="left", padx=4)
        self.cancel_btn = tk.Button(row, text="Cancel", command=self.cancel_work, state="disabled")
        self.cancel_btn.pack(side="left", padx=4)

        tk.Button(self, text="Freeze for 3 s (no thread)", command=self.freeze).pack(pady=6)
        self.log = tk.Listbox(self, height=6)
        self.log.pack(fill="both", expand=True, padx=8, pady=8)

    # ----- the clock proves the window stays responsive -----
    def tick_clock(self):
        self.clock.config(text=time.strftime("%H:%M:%S"))
        self.after(200, self.tick_clock)

    # ----- the worker thread: NEVER touch widgets here -----
    def work(self):
        try:
            total = 0
            for i in range(1, STEPS + 1):
                if self.cancel_flag.is_set():
                    self.messages.put(("cancelled", i - 1))
                    return
                time.sleep(0.05)
                total += i
                self.messages.put(("progress", i))
            self.messages.put(("done", total))
        except Exception as e:
            self.messages.put(("error", f"{type(e).__name__}: {e}"))

    # ----- the main thread: reads messages and updates the widgets -----
    def poll(self):
        try:
            while True:
                kind, value = self.messages.get_nowait()
                if kind == "progress":
                    self.bar["value"] = value
                    self.status.config(text=f"Working... {value}%")
                else:
                    text = {"done": f"Done. Result = {value}",
                            "cancelled": f"Cancelled at {value}%",
                            "error": f"Error: {value}"}[kind]
                    self.status.config(text=text)
                    self.log.insert(tk.END, text)
                    self.start_btn.config(state="normal")
                    self.cancel_btn.config(state="disabled")
        except queue.Empty:
            pass
        self.after(50, self.poll)

    def start_work(self):
        if self.worker is not None and self.worker.is_alive():
            return
        self.cancel_flag.clear()
        self.bar["value"] = 0
        self.start_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        self.worker = threading.Thread(target=self.work, name="Worker", daemon=True)
        self.worker.start()

    def cancel_work(self):
        self.cancel_flag.set()

    def freeze(self):
        self.status.config(text="Frozen...")
        time.sleep(3)                         # blocks the event loop: the clock stops and clicks wait
        self.status.config(text="Unfroze")

    def on_close(self):
        self.cancel_flag.set()
        self.destroy()                        # the worker is a daemon, so it cannot block the exit

if __name__ == "__main__":
    App().mainloop()