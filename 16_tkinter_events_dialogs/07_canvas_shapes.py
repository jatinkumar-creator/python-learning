import random
import tkinter as tk

W, H = 520, 340

root = tk.Tk()
root.title("Canvas shapes")

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack(padx=8, pady=8)
status = tk.Label(root, text="Click a shape to recolour it, drag to move it", anchor="w")
status.pack(fill="x", padx=8)

# Every create_* call returns an integer item id. Tags group items
canvas.create_rectangle(20, 20, 140, 90, fill="lightblue", outline="navy", width=3, tags=("shape", "box"))
canvas.create_oval(170, 20, 290, 90, fill="gold", tags=("shape", "disc"))
canvas.create_polygon(330, 90, 390, 20, 450, 90, fill="lightgreen", outline="darkgreen", tags="shape")
canvas.create_arc(20, 130, 120, 230, start=30, extent=240, fill="salmon", tags="shape")
canvas.create_line(20, 120, 480, 120, fill="gray", dash=(4, 3), width=2)
canvas.create_text(300, 170, text="Canvas text", font=("Arial", 14, "bold"))

# An image on a canvas (keep the reference on the canvas)
badge = tk.PhotoImage(width=40, height=40)
for row in range(4):
    for col in range(4):
        badge.put("#c0392b" if (row + col) % 2 else "#f1c40f",
                  to=(col * 10, row * 10, col * 10 + 10, row * 10 + 10))
canvas.create_image(470, 190, image=badge)
canvas.badge = badge

last = {"x": 0, "y": 0}

def random_colour():
    return "#%06x" % random.randint(0, 0xFFFFFF)

def press(event):
    item = canvas.find_withtag("current")[0]               # the item under the pointer
    last.update(x=event.x, y=event.y)
    canvas.tag_raise(item)                                  # bring it to the front
    canvas.itemconfig(item, fill=random_colour())
    status.config(text=f"item {item} ({canvas.type(item)}) at ({event.x}, {event.y})")

def drag(event):
    item = canvas.find_withtag("current")[0]
    canvas.move(item, event.x - last["x"], event.y - last["y"])
    last.update(x=event.x, y=event.y)

canvas.tag_bind("shape", "<Button-1>", press)
canvas.tag_bind("shape", "<B1-Motion>", drag)
canvas.tag_bind("shape", "<Enter>", lambda e: canvas.config(cursor="hand2"))
canvas.tag_bind("shape", "<Leave>", lambda e: canvas.config(cursor=""))

# A bouncing ball with after()
ball = canvas.create_oval(300, 220, 330, 250, fill="tomato", outline="")
speed = {"x": 4, "y": 3}

def animate():
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 + speed["x"] < 0 or x2 + speed["x"] > W:
        speed["x"] = -speed["x"]
    if y1 + speed["y"] < 0 or y2 + speed["y"] > H:
        speed["y"] = -speed["y"]
    canvas.move(ball, speed["x"], speed["y"])
    root.after(16, animate)

animate()

row = tk.Frame(root)
row.pack(pady=4)
tk.Button(row, text="Add circle", command=lambda: canvas.create_oval(
    random.randint(0, W - 40), random.randint(130, H - 40), 0, 0, fill=random_colour(), tags="shape")
    or None).pack(side="left", padx=3)
tk.Button(row, text="Delete all shapes", command=lambda: canvas.delete("shape")).pack(side="left", padx=3)

root.mainloop()