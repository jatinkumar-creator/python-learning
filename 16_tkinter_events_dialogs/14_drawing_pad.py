import json
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, messagebox

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)

class DrawingPad(tk.Tk):
    BG = "white"

    def __init__(self):
        super().__init__()
        self.title("Drawing pad")
        self.color = "#1f3a93"
        self.eraser = tk.BooleanVar(value=False)
        self.pen_width = tk.IntVar(value=4)
        self.strokes = []
        self.current = None
        self._build()
        self.bind("<Control-z>", lambda e: self.undo())

    def _build(self):
        bar = tk.Frame(self, padx=6, pady=6)
        bar.pack(fill="x")
        self.color_btn = tk.Button(bar, text="Colour...", command=self.choose_color,
                                   bg=self.color, fg="white")
        self.color_btn.pack(side="left", padx=2)
        tk.Scale(bar, from_=1, to=20, orient="horizontal", variable=self.pen_width,
                 label="Pen size", length=120).pack(side="left", padx=6)
        tk.Checkbutton(bar, text="Eraser", variable=self.eraser).pack(side="left", padx=2)
        for label, command in (("Undo", self.undo), ("Clear", self.clear),
                               ("Save...", self.save), ("Load...", self.load)):
            tk.Button(bar, text=label, command=command).pack(side="left", padx=2)

        self.status = tk.Label(self, text="Draw with the left mouse button", anchor="w", relief="sunken")
        self.status.pack(side="bottom", fill="x")
        self.canvas = tk.Canvas(self, width=700, height=420, bg=self.BG, cursor="pencil")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.start_stroke)
        self.canvas.bind("<B1-Motion>", self.extend_stroke)
        self.canvas.bind("<ButtonRelease-1>", self.end_stroke)

    def pen(self):
        if self.eraser.get():
            return self.BG, self.pen_width.get() * 3           # an "eraser" simply paints in the background colour
        return self.color, self.pen_width.get()

    def start_stroke(self, event):
        color, width = self.pen()
        r = width / 2
        dot = self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                                      fill=color, outline=color)
        self.current = {"color": color, "width": width, "points": [(event.x, event.y)], "items": [dot]}

    def extend_stroke(self, event):
        if self.current is None:
            return
        x0, y0 = self.current["points"][-1]
        line = self.canvas.create_line(x0, y0, event.x, event.y, fill=self.current["color"],
                                       width=self.current["width"], capstyle="round")
        self.current["points"].append((event.x, event.y))
        self.current["items"].append(line)

    def end_stroke(self, event):
        if self.current is not None:
            self.strokes.append(self.current)
            self.current = None
        self.say(f"{len(self.strokes)} stroke(s)")

    def say(self, message):
        self.status.config(text=message)

    def choose_color(self):
        chosen = colorchooser.askcolor(color=self.color, parent=self)[1]      # (None, None) when cancelled
        if chosen:
            self.color = chosen
            self.eraser.set(False)
            self.color_btn.config(bg=chosen)

    def undo(self):
        if not self.strokes:
            self.say("Nothing to undo")
            return
        stroke = self.strokes.pop()
        for item in stroke["items"]:
            self.canvas.delete(item)
        self.say(f"{len(self.strokes)} stroke(s)")

    def clear(self):
        self.canvas.delete("all")
        self.strokes.clear()
        self.say("Cleared")

    def draw_stroke(self, stroke):
        x, y = stroke["points"][0]
        r = stroke["width"] / 2
        stroke["items"].append(self.canvas.create_oval(
            x - r, y - r, x + r, y + r, fill=stroke["color"], outline=stroke["color"]))
        for (x0, y0), (x1, y1) in zip(stroke["points"], stroke["points"][1:]):
            stroke["items"].append(self.canvas.create_line(
                x0, y0, x1, y1, fill=stroke["color"], width=stroke["width"], capstyle="round"))

    def save(self):
        path = filedialog.asksaveasfilename(parent=self, initialdir=str(SCRATCH), initialfile="drawing.json",
                                            defaultextension=".json", filetypes=[("Drawing", "*.json")])
        if not path:
            return
        data = [{"color": s["color"], "width": s["width"], "points": s["points"]} for s in self.strokes]
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"version": 1, "strokes": data}, f)
        except OSError as e:
            messagebox.showerror("Cannot save", f"{type(e).__name__}: {e}", parent=self)
            return
        self.say(f"Saved {Path(path).name}")

    def load(self):
        path = filedialog.askopenfilename(parent=self, initialdir=str(SCRATCH),
                                          filetypes=[("Drawing", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            strokes = []
            for s in data["strokes"]:
                points = [tuple(p) for p in s["points"]]
                if not points:
                    raise ValueError("a stroke has no points")
                strokes.append({"color": s["color"], "width": int(s["width"]), "points": points, "items": []})
            self.clear()
            for stroke in strokes:
                self.draw_stroke(stroke)
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError, tk.TclError) as e:
            self.clear()
            messagebox.showerror("Cannot load drawing", f"{type(e).__name__}: {e}", parent=self)
            return
        self.strokes = strokes
        self.say(f"Loaded {Path(path).name}: {len(strokes)} stroke(s)")

if __name__ == "__main__":
    DrawingPad().mainloop()