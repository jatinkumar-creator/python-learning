import re
import tkinter as tk
from tkinter import ttk

SAMPLE = ("Contact: asha.k@example.com, ravi_87@shop.co.in\n"
          "Call +91 9876543210 on 2026-10-27.\n")
FLAGS = {"IGNORECASE": re.I, "MULTILINE": re.M, "DOTALL": re.S, "VERBOSE": re.X, "ASCII": re.A}
MAX_MATCHES = 500

class RegexTester(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Regex tester")
        self.geometry("780x660")
        self.pattern = tk.StringVar(value=r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
        self.replacement = tk.StringVar(value="[EMAIL]")
        self.flag_vars = {name: tk.BooleanVar() for name in FLAGS}
        self.spans = {}
        self._build()
        for var in (self.pattern, self.replacement, *self.flag_vars.values()):
            var.trace_add("write", lambda *args: self.update_results())
        self.update_results()

    def _build(self):
        top = tk.Frame(self, padx=8, pady=6)
        top.pack(fill="x")
        tk.Label(top, text="Pattern").grid(row=0, column=0, sticky="w")
        tk.Entry(top, textvariable=self.pattern, font=("Consolas", 12)).grid(
            row=0, column=1, sticky="ew", padx=6)
        tk.Label(top, text="Replace with").grid(row=1, column=0, sticky="w")
        tk.Entry(top, textvariable=self.replacement, font=("Consolas", 12)).grid(
            row=1, column=1, sticky="ew", padx=6, pady=4)
        top.columnconfigure(1, weight=1)

        flags = tk.Frame(self, padx=8)
        flags.pack(fill="x")
        for name, var in self.flag_vars.items():
            tk.Checkbutton(flags, text=name, variable=var).pack(side="left", padx=4)

        self.status = tk.Label(self, anchor="w", padx=8, pady=4)
        self.status.pack(fill="x")

        tk.Label(self, text="Test text (edit me)", anchor="w", padx=8).pack(fill="x")
        self.text = tk.Text(self, height=9, font=("Consolas", 11), wrap="word", undo=True)
        self.text.pack(fill="x", padx=8)
        self.text.insert("1.0", SAMPLE)
        self.text.edit_reset()
        self.text.edit_modified(False)
        self.text.tag_configure("hit", background="#ffe08a")
        self.text.tag_configure("hit_alt", background="#a8e6a1")
        self.text.tag_configure("current", background="#ff9f80")       # created last, so it has the top priority
        self.text.bind("<<Modified>>", self.on_text_modified)

        tk.Label(self, text="Matches (click a row to locate it)", anchor="w", padx=8).pack(
            fill="x", pady=(8, 0))
        holder = tk.Frame(self, padx=8)
        holder.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(holder, columns=("n", "span", "match", "groups"),
                                 show="headings", height=7)
        for key, title, width in (("n", "#", 40), ("span", "Span", 80),
                                  ("match", "Match", 230), ("groups", "Groups", 380)):
            self.tree.heading(key, text=title)
            self.tree.column(key, width=width, anchor="w")
        scroll = ttk.Scrollbar(holder, orient="vertical", command=self.tree.yview)
        self.tree.config(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        tk.Label(self, text="Replacement preview", anchor="w", padx=8).pack(fill="x", pady=(8, 0))
        self.preview = tk.Text(self, height=5, font=("Consolas", 11), wrap="word",
                               state="disabled", bg="#f4f4f4")
        self.preview.pack(fill="x", padx=8, pady=(0, 8))

    def say(self, message, colour="black"):
        self.status.config(text=message, fg=colour)

    def set_preview(self, content):
        self.preview.config(state="normal")
        self.preview.delete("1.0", tk.END)
        self.preview.insert("1.0", content)
        self.preview.config(state="disabled")

    def on_text_modified(self, event=None):
        if self.text.edit_modified():
            self.text.edit_modified(False)             # reset the flag, or the event never fires again
            self.update_results()

    def on_select(self, event=None):
        self.text.tag_remove("current", "1.0", tk.END)
        selection = self.tree.selection()
        if not selection:
            return
        start, end = self.spans[selection[0]]
        if end > start:
            self.text.tag_add("current", f"1.0+{start}c", f"1.0+{end}c")
            self.text.see(f"1.0+{start}c")

    def update_results(self):
        for tag in ("hit", "hit_alt", "current"):
            self.text.tag_remove(tag, "1.0", tk.END)
        self.tree.delete(*self.tree.get_children())
        self.spans.clear()

        pattern = self.pattern.get()
        if not pattern:
            self.say("Type a pattern above", "gray")
            self.set_preview("")
            return

        flags = 0
        for name, var in self.flag_vars.items():
            if var.get():
                flags |= FLAGS[name]
        try:
            compiled = re.compile(pattern, flags)
        except re.error as e:
            self.say(f"Invalid pattern: {e}", "red")
            self.set_preview("")
            return

        content = self.text.get("1.0", "end-1c")
        count, truncated = 0, False
        for m in compiled.finditer(content):
            if count >= MAX_MATCHES:
                truncated = True
                break
            count += 1
            start, end = m.span()
            if end > start:                            # empty matches have nothing to highlight
                self.text.tag_add("hit" if count % 2 else "hit_alt", f"1.0+{start}c", f"1.0+{end}c")
            groups = m.groupdict() if compiled.groupindex else m.groups()
            iid = self.tree.insert("", tk.END, values=(
                count, f"{start}-{end}", repr(m.group()), repr(groups) if compiled.groups else ""))
            self.spans[iid] = (start, end)

        note = f" (showing the first {MAX_MATCHES})" if truncated else ""
        self.say(f"{count} match{'es' if count != 1 else ''}{note}",
                 "darkgreen" if count else "gray")

        try:
            self.set_preview(compiled.sub(self.replacement.get(), content))
        except (re.error, IndexError) as e:
            self.set_preview(f"Replacement error: {e}")

if __name__ == "__main__":
    RegexTester().mainloop()