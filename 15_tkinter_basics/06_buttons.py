import tkinter as tk

root = tk.Tk()
root.title("Buttons")
root.geometry("420x420")

log = tk.Label(root, text="(nothing yet)", font=("Arial", 12))
log.pack(pady=10)

def say(message):
    log.config(text=message)

# 1. command takes the FUNCTION itself, not a call to it
def hello():
    print("hello() ran")

tk.Button(root, text="Correct: command=hello", command=hello).pack(pady=2)
tk.Button(root, text="Wrong: command=hello()", command=hello()).pack(pady=2)
# The wrong one printed "hello() ran" at STARTUP, and clicking it does nothing

# 2. Passing arguments with lambda
tk.Button(root, text="Say hi", command=lambda: say("hi!")).pack(pady=2)

# 3. The loop trap (late binding), and the fix
row = tk.Frame(root)
row.pack(pady=5)
for i in range(3):
    tk.Button(row, text=f"Trap {i}", command=lambda: say(f"trap says {i}")).pack(side="left", padx=2)
for i in range(3):
    tk.Button(row, text=f"Fix {i}", command=lambda i=i: say(f"fix says {i}")).pack(side="left", padx=2)

# 4. A counter, with a disabled state
count = 0
counter_label = tk.Label(root, text="Clicks: 0")
counter_label.pack()

def click():
    global count
    count += 1
    counter_label.config(text=f"Clicks: {count}")
    if count >= 5:
        counter_btn.config(state="disabled", text="Limit reached")

counter_btn = tk.Button(root, text="Click me (max 5)", command=click)
counter_btn.pack(pady=5)

# 5. Styling
tk.Button(root, text="Styled", bg="seagreen", fg="white", font=("Arial", 11, "bold"),
          width=12, relief="raised", cursor="hand2").pack(pady=5)

tk.Button(root, text="Quit", command=root.destroy).pack(pady=10)
root.mainloop()