import csv
import json
import math
import tkinter as tk
from datetime import date, datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

DATA_DIR = Path(__file__).resolve().parent / "scratch"
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "expenses.json"
CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Health", "Other"]

class ExpenseError(Exception):
    """A problem with user input, with a message that is safe to show."""

def parse_expense(date_text, category, amount_text, note):
    try:
        when = datetime.strptime(date_text.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ExpenseError("Date must look like 2026-10-27") from None
    if category not in CATEGORIES:
        raise ExpenseError("Pick a category from the list")
    try:
        amount = round(float(amount_text.replace(",", "")), 2)
    except ValueError:
        raise ExpenseError("Amount must be a number") from None
    if not (math.isfinite(amount) and amount > 0):
        raise ExpenseError("Amount must be greater than zero")
    return {"date": when.isoformat(), "category": category, "amount": amount, "note": note.strip()}

class ExpenseStore:
    def __init__(self, path):
        self.path = path
        self.items = []
        self.next_id = 1

    def load(self):
        """Return None when all is well, or a message when a damaged file had to be set aside."""
        if not self.path.exists():
            return None
        try:
            with open(self.path, encoding="utf-8") as f:
                raw = json.load(f)
            items = [{"id": int(x["id"]),
                      **parse_expense(x["date"], x["category"], str(x["amount"]), x.get("note", ""))}
                     for x in raw]
        except (json.JSONDecodeError, KeyError, TypeError, ValueError, ExpenseError) as e:
            backup = self.path.with_suffix(".bad")
            self.path.replace(backup)
            return (f"{self.path.name} was damaged ({type(e).__name__}). It was kept as "
                    f"{backup.name} and a new list was started.")
        self.items = items
        self.next_id = max((i["id"] for i in items), default=0) + 1
        return None

    def save(self):
        tmp = self.path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:           # write a temporary copy...
            json.dump(self.items, f, indent=2)
        tmp.replace(self.path)                                # ...then swap it in, so a crash cannot leave half a file

    def add(self, data):
        item = {"id": self.next_id, **data}
        self.next_id += 1
        self.items.append(item)
        try:
            self.save()
        except OSError:
            self.items.remove(item)                           # roll back, so memory matches the disk
            raise
        return item

    def delete(self, ids):
        self.items = [i for i in self.items if i["id"] not in ids]
        self.save()

class ExpenseApp(tk.Tk):
    COLUMNS = (("date", "Date", 100, "w"), ("category", "Category", 110, "w"),
               ("amount", "Amount", 100, "e"), ("note", "Note", 260, "w"))

    def __init__(self):
        super().__init__()
        self.title("Expense tracker")
        self.geometry("680x520")
        self.store = ExpenseStore(DATA_FILE)
        self.date = tk.StringVar(value=date.today().isoformat())
        self.category = tk.StringVar(value=CATEGORIES[0])
        self.amount = tk.StringVar()
        self.note = tk.StringVar()
        self.view = tk.StringVar(value="All")
        self.sort_column, self.sort_reverse = "date", False
        self._build()
        message = self.store.load()
        if message:
            messagebox.showwarning("Data problem", message, parent=self)
        self.refresh()

    def _build(self):
        form = tk.LabelFrame(self, text="New expense", padx=8, pady=8)
        form.pack(fill="x", padx=8, pady=8)
        tk.Label(form, text="Date").grid(row=0, column=0, sticky="w")
        tk.Entry(form, textvariable=self.date, width=12).grid(row=0, column=1, padx=4)
        tk.Label(form, text="Category").grid(row=0, column=2, sticky="w")
        ttk.Combobox(form, textvariable=self.category, values=CATEGORIES, state="readonly",
                     width=10).grid(row=0, column=3, padx=4)
        tk.Label(form, text="Amount").grid(row=1, column=0, sticky="w", pady=4)
        self.amount_entry = tk.Entry(form, textvariable=self.amount, width=12)
        self.amount_entry.grid(row=1, column=1, padx=4)
        tk.Label(form, text="Note").grid(row=1, column=2, sticky="w")
        note_entry = tk.Entry(form, textvariable=self.note, width=28)
        note_entry.grid(row=1, column=3, padx=4)
        tk.Button(form, text="Add", width=8, command=self.add_expense).grid(row=1, column=4, padx=6)
        self.amount_entry.bind("<Return>", lambda e: self.add_expense())
        note_entry.bind("<Return>", lambda e: self.add_expense())

        filter_bar = tk.Frame(self)
        filter_bar.pack(fill="x", padx=8)
        tk.Label(filter_bar, text="Show:").pack(side="left")
        chooser = ttk.Combobox(filter_bar, textvariable=self.view, values=["All"] + CATEGORIES,
                               state="readonly", width=12)
        chooser.pack(side="left", padx=4)
        chooser.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        self.status = tk.Label(self, text="", anchor="w", relief="sunken", padx=6)
        self.status.pack(side="bottom", fill="x")
        self.total = tk.Label(self, text="", anchor="w", font=("Arial", 11, "bold"), padx=8)
        self.total.pack(side="bottom", fill="x")

        buttons = tk.Frame(self, padx=8, pady=4)
        buttons.pack(side="bottom", fill="x")
        tk.Button(buttons, text="Delete selected", command=self.delete_selected).pack(side="left")
        tk.Button(buttons, text="Export CSV...", command=self.export_csv).pack(side="left", padx=6)

        holder = tk.Frame(self, padx=8, pady=4)
        holder.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(holder, columns=[c[0] for c in self.COLUMNS], show="headings",
                                 selectmode="extended")
        for key, title, width, anchor in self.COLUMNS:
            self.tree.heading(key, text=title, command=lambda k=key: self.sort_by(k))
            self.tree.column(key, width=width, anchor=anchor)
        scroll = ttk.Scrollbar(holder, orient="vertical", command=self.tree.yview)
        self.tree.config(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Delete>", lambda e: self.delete_selected())

    def say(self, message, error=False):
        self.status.config(text=message, fg="red" if error else "black")

    def visible_items(self):
        items = self.store.items
        if self.view.get() != "All":
            items = [i for i in items if i["category"] == self.view.get()]
        return sorted(items, key=lambda i: i[self.sort_column], reverse=self.sort_reverse)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        items = self.visible_items()
        for item in items:
            self.tree.insert("", tk.END, iid=str(item["id"]),
                             values=(item["date"], item["category"], f"{item['amount']:,.2f}", item["note"]))
        total = sum(i["amount"] for i in items)
        self.total.config(text=f"Total ({self.view.get()}): {total:,.2f}   across {len(items)} item(s)")

    def sort_by(self, column):
        if column == self.sort_column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column, self.sort_reverse = column, False
        self.refresh()

    def add_expense(self):
        try:
            data = parse_expense(self.date.get(), self.category.get(), self.amount.get(), self.note.get())
            self.store.add(data)
        except ExpenseError as e:
            self.say(str(e), error=True)
            return
        except OSError as e:
            messagebox.showerror("Cannot save", f"{type(e).__name__}: {e}", parent=self)
            return
        self.amount.set("")
        self.note.set("")
        self.refresh()
        self.say("Expense added")
        self.amount_entry.focus()

    def delete_selected(self):
        ids = {int(iid) for iid in self.tree.selection()}
        if not ids:
            self.say("Select one or more rows first", error=True)
            return
        if not messagebox.askyesno("Delete", f"Delete {len(ids)} expense(s)?", icon="warning", parent=self):
            return
        try:
            self.store.delete(ids)
        except OSError as e:
            messagebox.showerror("Cannot save", f"{type(e).__name__}: {e}", parent=self)
            return
        self.refresh()
        self.say(f"Deleted {len(ids)} expense(s)")

    def export_csv(self):
        path = filedialog.asksaveasfilename(parent=self, initialdir=str(DATA_DIR), initialfile="expenses.csv",
                                            defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "category", "amount", "note"])
                for i in self.visible_items():
                    writer.writerow([i["date"], i["category"], f"{i['amount']:.2f}", i["note"]])
        except OSError as e:
            messagebox.showerror("Cannot export", f"{type(e).__name__}: {e}", parent=self)
            return
        self.say(f"Exported to {Path(path).name}")

if __name__ == "__main__":
    ExpenseApp().mainloop()