import tkinter as tk

root = tk.Tk()
root.title("Event inspector")
root.geometry("480x340")

info = tk.StringVar(value="Click, type, scroll, or move the mouse in the grey area")
tk.Label(root, textvariable=info, justify="left", anchor="w",
         font=("Consolas", 10), wraplength=460).pack(fill="x", padx=8, pady=6)

area = tk.Frame(root, bg="lightgray", width=460, height=200)
area.pack(padx=8, pady=4)
area.pack_propagate(False)

position = tk.Label(root, text="pointer: (-, -)")
position.pack(anchor="w", padx=8)

def show(text):
    info.set(text)
    print(text)

def on_click(event):
    area.focus_set()                      # a Frame receives key events only if it has the focus
    show(f"click   button={event.num} x={event.x} y={event.y} "
         f"screen=({event.x_root},{event.y_root})")
    print("   ", event)                   # the full text form of the event

def on_double(event):
    show(f"double-click at ({event.x}, {event.y})")

def on_key(event):
    show(f"key     char={event.char!r} keysym={event.keysym!r} keycode={event.keycode}")

def on_motion(event):
    position.config(text=f"pointer: ({event.x}, {event.y})")

def on_wheel(event):
    show(f"wheel   delta={event.delta} ({'up' if event.delta > 0 else 'down'})")

area.bind("<Button-1>", on_click)
area.bind("<Button-3>", on_click)          # the right button on Windows
area.bind("<Double-Button-1>", on_double)
area.bind("<Key>", on_key)
area.bind("<Motion>", on_motion)
area.bind("<MouseWheel>", on_wheel)
area.bind("<Leave>", lambda e: position.config(text="pointer: left the area"))
area.focus_set()

root.mainloop()