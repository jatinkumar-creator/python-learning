# from git bash - 
#python -m pip install pillow
#python -m pip show pillow

import sys
import tkinter as tk
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageTk
except ModuleNotFoundError:
    sys.exit("Pillow is not installed. With (venv) active run: python -m pip install pillow")

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)

photo = Image.new("RGB", (400, 240), "steelblue")
draw = ImageDraw.Draw(photo)
draw.ellipse((120, 40, 280, 200), fill="gold", outline="white", width=4)
draw.text((20, 10), "Made with Pillow", fill="white")
jpg_path = SCRATCH / "sample.jpg"
photo.save(jpg_path, quality=90)
print(photo.size, photo.mode, jpg_path.stat().st_size, "bytes")

reopened = Image.open(jpg_path)
print(reopened.format, reopened.size)
thumb = reopened.copy()
thumb.thumbnail((160, 160))                       # shrinks in place and keeps the aspect ratio

root = tk.Tk()
root.title("Pillow")

variants = [(thumb, "thumbnail"),
            (thumb.convert("L"), "greyscale"),
            (thumb.rotate(30, expand=True), "rotated 30 degrees")]
for column, (img, caption) in enumerate(variants):
    tk_image = ImageTk.PhotoImage(img)                # needs the Tk root to exist first
    label = tk.Label(root, image=tk_image, compound="top", text=caption)
    label.image = tk_image                            # keep the reference
    label.grid(row=0, column=column, padx=6, pady=6)

root.mainloop()