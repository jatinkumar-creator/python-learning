import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)

SUPPORTED = {".png", ".gif", ".ppm", ".pgm"}
STEPS = [(1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1)]     # (zoom, subsample): scale = zoom / subsample
START_STEP = 3

class Viewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image viewer")
        self.geometry("720x520")
        self.original = None          # the PhotoImage as loaded
        self.shown = None             # the scaled PhotoImage on the canvas: kept as an attribute so it is not deleted
        self.path = None
        self.step = START_STEP
        self._build()
        self.bind("<Left>", lambda e: self.neighbour(-1))
        self.bind("<Right>", lambda e: self.neighbour(+1))
        self.bind("<plus>", lambda e: self.change_zoom(+1))
        self.bind("<equal>", lambda e: self.change_zoom(+1))          # "+" without Shift on most keyboards
        self.bind("<minus>", lambda e: self.change_zoom(-1))
        self.bind("<Key-0>", lambda e: self.change_zoom(0))
        self.bind("<Control-o>", lambda e: self.open_dialog())

    def _build(self):
        bar = tk.Frame(self, padx=6, pady=6)
        bar.pack(fill="x")
        for label, command in (("Open...", self.open_dialog), ("Previous", lambda: self.neighbour(-1)),
                               ("Next", lambda: self.neighbour(+1)), ("Zoom -", lambda: self.change_zoom(-1)),
                               ("Zoom +", lambda: self.change_zoom(+1)), ("100%", lambda: self.change_zoom(0))):
            tk.Button(bar, text=label, command=command).pack(side="left", padx=2)

        self.status = tk.Label(self, text="Open a PNG or GIF file (Ctrl+O)", anchor="w", relief="sunken")
        self.status.pack(side="bottom", fill="x")

        holder = tk.Frame(self)
        holder.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(holder, bg="gray25", highlightthickness=0)
        ybar = tk.Scrollbar(holder, orient="vertical", command=self.canvas.yview)
        xbar = tk.Scrollbar(holder, orient="horizontal", command=self.canvas.xview)
        self.canvas.config(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
        holder.rowconfigure(0, weight=1)
        holder.columnconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        ybar.grid(row=0, column=1, sticky="ns")
        xbar.grid(row=1, column=0, sticky="ew")

    def open_dialog(self):
        path = filedialog.askopenfilename(
            parent=self, initialdir=str(self.path.parent if self.path else SCRATCH),
            filetypes=[("Images", "*.png *.gif *.ppm *.pgm"), ("All files", "*.*")])
        if path:
            self.load(Path(path))

    def load(self, path):
        try:
            image = tk.PhotoImage(file=str(path))
        except tk.TclError as e:
            messagebox.showerror("Cannot open image",
                                 f"{path.name}\n\n{e}\n\nPlain Tkinter reads PNG, GIF, PGM and PPM. "
                                 "Use Pillow for JPEG.", parent=self)
            return
        self.original, self.path, self.step = image, path, START_STEP
        self.render()

    def render(self):
        if self.original is None:
            return
        zoom, sub = STEPS[self.step]
        image = self.original
        if zoom > 1:
            image = image.zoom(zoom)
        if sub > 1:
            image = image.subsample(sub)
        self.shown = image
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.shown)
        self.canvas.config(scrollregion=(0, 0, image.width(), image.height()))
        self.status.config(
            text=f"{self.path.name}  |  original {self.original.width()}x{self.original.height()}"
                 f"  |  shown {image.width()}x{image.height()}  |  scale {zoom}/{sub}")

    def change_zoom(self, direction):
        if direction == 0:
            self.step = START_STEP
        else:
            self.step = min(max(self.step + direction, 0), len(STEPS) - 1)
        self.render()

    def neighbour(self, offset):
        if self.path is None:
            return
        files = sorted(p for p in self.path.parent.iterdir() if p.suffix.lower() in SUPPORTED)
        if len(files) < 2:
            return
        index = files.index(self.path) if self.path in files else 0
        self.load(files[(index + offset) % len(files)])

if __name__ == "__main__":
    Viewer().mainloop()