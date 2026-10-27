import time
import tkinter as tk

root = tk.Tk()
root.title("sleep vs after")
root.geometry("400x260")

clock = tk.Label(root, font=("Consolas", 16))
clock.pack(pady=8)

def update_clock():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_clock)          # schedule myself again: a loop that never blocks

update_clock()

status = tk.Label(root, text="Ready", font=("Arial", 12))
status.pack(pady=8)

def freeze():
    status.config(text="Working...")        # you will never even see this text
    time.sleep(4)                           # blocks the event loop: no repaint, no clicks, no clock
    status.config(text="Done, but the window was frozen and the clock stopped")

remaining = 0

def tick():
    global remaining
    if remaining > 0:
        status.config(text=f"{remaining} seconds left")
        remaining -= 1
        root.after(1000, tick)              # run tick() again in 1000 ms, then return immediately
    else:
        status.config(text="Done: the window stayed responsive")
        start_btn.config(state="normal")

def start():
    global remaining
    remaining = 4
    start_btn.config(state="disabled")      # stop a second click starting a second countdown
    tick()

tk.Button(root, text="Freeze for 4 s (time.sleep)", command=freeze).pack(pady=3)
start_btn = tk.Button(root, text="Count down 4 s (after)", command=start)
start_btn.pack(pady=3)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=3)

root.mainloop()