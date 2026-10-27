import hashlib
import hmac
import tkinter as tk
from tkinter import messagebox

def digest(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

USERS = {"asha": digest("python123"), "ravi": digest("tkinter!")}     # demo only
MAX_ATTEMPTS = 3
LOCK_SECONDS = 5

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(False, False)
        self.attempts = 0
        self.locked = False
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.reveal = tk.BooleanVar(value=False)
        self._build()
        self.bind("<Return>", lambda e: self.login())
        self.bind("<Escape>", lambda e: self.destroy())

    def _build(self):
        frame = tk.Frame(self, padx=20, pady=15)
        frame.grid()
        tk.Label(frame, text="Username").grid(row=0, column=0, sticky="e", pady=4)
        self.user_entry = tk.Entry(frame, textvariable=self.user, width=22)
        self.user_entry.grid(row=0, column=1, padx=6)
        tk.Label(frame, text="Password").grid(row=1, column=0, sticky="e", pady=4)
        self.pwd_entry = tk.Entry(frame, textvariable=self.password, show="*", width=22)
        self.pwd_entry.grid(row=1, column=1, padx=6)
        tk.Checkbutton(frame, text="Show password", variable=self.reveal,
                       command=self.toggle_reveal).grid(row=2, column=1, sticky="w")
        self.login_btn = tk.Button(frame, text="Log in", width=10, command=self.login)
        self.login_btn.grid(row=3, column=1, sticky="w", pady=8)
        self.feedback = tk.Label(frame, text="", fg="red")
        self.feedback.grid(row=4, column=0, columnspan=2)
        self.user_entry.focus()

    def toggle_reveal(self):
        self.pwd_entry.config(show="" if self.reveal.get() else "*")

    def login(self):
        if self.locked:
            return
        name = self.user.get().strip().lower()
        pwd = self.password.get()
        if not name or not pwd:
            self.feedback.config(text="Enter both username and password")
            return
        stored = USERS.get(name)
        if stored and hmac.compare_digest(digest(pwd), stored):
            messagebox.showinfo("Welcome", f"Welcome back, {name.title()}!", parent=self)
            self.destroy()
            return
        self.attempts += 1
        self.password.set("")
        left = MAX_ATTEMPTS - self.attempts
        if left > 0:
            self.feedback.config(text=f"Wrong username or password ({left} attempts left)")
            self.pwd_entry.focus()
        else:
            self.lock(LOCK_SECONDS)

    def lock(self, seconds):
        self.locked = True
        self.login_btn.config(state="disabled")
        self.pwd_entry.config(state="disabled")
        self.countdown(seconds)

    def countdown(self, seconds):
        if seconds > 0:
            self.feedback.config(text=f"Too many attempts. Try again in {seconds} s")
            self.after(1000, self.countdown, seconds - 1)          # after(ms, function, *arguments)
        else:
            self.locked = False
            self.attempts = 0
            self.login_btn.config(state="normal")
            self.pwd_entry.config(state="normal")
            self.feedback.config(text="You can try again")
            self.pwd_entry.focus()

if __name__ == "__main__":
    LoginApp().mainloop()