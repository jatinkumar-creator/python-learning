import tkinter as tk
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)

root = tk.Tk()
root.title("Images")

# 1. Draw images pixel by pixel: put(colour, to=(x1, y1, x2, y2)) fills a rectangle (x2 and y2 are excluded)
gradient = tk.PhotoImage(width=240, height=100)
for y in range(100):
    shade = int(255 * y / 99)
    gradient.put(f"#{shade:02x}40{255 - shade:02x}", to=(0, y, 240, y + 1))

board = tk.PhotoImage(width=80, height=80)
for row in range(8):
    for col in range(8):
        colour = "#222222" if (row + col) % 2 == 0 else "#eeeeee"
        board.put(colour, to=(col * 10, row * 10, col * 10 + 10, row * 10 + 10))

# 2. Save to disk, then load back
gradient_path = SCRATCH / "gradient.png"
gradient.write(str(gradient_path), format="png")
board.write(str(SCRATCH / "board.png"), format="png")
print("saved", gradient_path.name, gradient_path.stat().st_size, "bytes")
loaded = tk.PhotoImage(file=str(gradient_path))
print("loaded size:", loaded.width(), "x", loaded.height())

# 3. zoom() makes an image bigger and subsample() smaller, by whole-number factors
zoomed = board.zoom(3)
shrunk = gradient.subsample(2)
print("board", board.width(), "->", zoomed.width(), "| gradient", gradient.width(), "->", shrunk.width())

# 4. Show them. Keep a reference on the label, or the picture disappears
def add(image, caption, row, column):
    holder = tk.Frame(root, padx=6, pady=6)
    holder.grid(row=row, column=column)
    label = tk.Label(holder, image=image, relief="sunken")
    label.pack()
    label.image = image                                   # KEEP A REFERENCE
    tk.Label(holder, text=f"{caption}\n{image.width()}x{image.height()}").pack()

add(gradient, "drawn gradient", 0, 0)
add(loaded, "loaded from PNG", 0, 1)
add(zoomed, "board.zoom(3)", 1, 0)
add(shrunk, "gradient.subsample(2)", 1, 1)

tk.Button(root, text=" Button with an image", image=board, compound="left").grid(
    row=2, column=0, columnspan=2, pady=6)

# 5. The reference trap
def show_broken():
    img = tk.PhotoImage(file=str(gradient_path))          # a LOCAL variable
    tk.Label(root, image=img, text="no reference kept", compound="top").grid(row=3, column=0)
    # when this function returns, img has no references left and Python deletes it

def show_fixed():
    img = tk.PhotoImage(file=str(gradient_path))
    label = tk.Label(root, image=img, text="reference kept", compound="top")
    label.image = img
    label.grid(row=3, column=1)

tk.Button(root, text="Show broken", command=show_broken).grid(row=4, column=0, pady=6)
tk.Button(root, text="Show fixed", command=show_fixed).grid(row=4, column=1, pady=6)

root.mainloop()