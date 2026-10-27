import random
import tkinter as tk

W, H, SIZE, STEP, DELAY = 420, 300, 30, 4, 16

root = tk.Tk()
root.title("Move the square")

canvas = tk.Canvas(root, width=W, height=H, bg="white", highlightthickness=0)
canvas.pack()

START = ((W - SIZE) // 2, (H - SIZE) // 2)
square = canvas.create_rectangle(START[0], START[1], START[0] + SIZE, START[1] + SIZE,
                                 fill="tomato", outline="")

tk.Label(root, text="Arrow keys or WASD to move, Space = new colour, R = reset").pack()
coords_label = tk.Label(root, text="")
coords_label.pack()

DIRECTIONS = {"Left": (-1, 0), "Right": (1, 0), "Up": (0, -1), "Down": (0, 1),
              "a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1)}
pressed = set()

def normalise(keysym):
    return keysym.lower() if len(keysym) == 1 else keysym

def key_down(event):
    pressed.add(normalise(event.keysym))

def key_up(event):
    pressed.discard(normalise(event.keysym))

def change_colour(event=None):
    colour = "#%02x%02x%02x" % tuple(random.randint(60, 230) for _ in range(3))
    canvas.itemconfig(square, fill=colour)

def reset(event=None):
    canvas.coords(square, START[0], START[1], START[0] + SIZE, START[1] + SIZE)

def game_loop():
    dx = sum(DIRECTIONS[k][0] for k in pressed if k in DIRECTIONS)
    dy = sum(DIRECTIONS[k][1] for k in pressed if k in DIRECTIONS)
    x1, y1, x2, y2 = canvas.coords(square)
    if dx or dy:
        new_x = min(max(x1 + dx * STEP, 0), W - SIZE)       # clamp inside the canvas
        new_y = min(max(y1 + dy * STEP, 0), H - SIZE)
        canvas.move(square, new_x - x1, new_y - y1)
    x1, y1, *_ = canvas.coords(square)
    coords_label.config(text=f"x={x1:.0f}  y={y1:.0f}")
    root.after(DELAY, game_loop)                              # run again in 16 ms: about 60 frames a second

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
root.bind("<space>", change_colour)
root.bind("<r>", reset)
root.bind("<FocusOut>", lambda e: pressed.clear())            # a key released elsewhere must not stay "stuck"

game_loop()
root.mainloop()