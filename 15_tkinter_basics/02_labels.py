import tkinter as tk

root = tk.Tk()
root.title("Labels")
root.geometry("440x420")

tk.Label(root, text="Plain label").pack()
tk.Label(root, text="Styled", font=("Arial", 18, "bold"),
         fg="white", bg="steelblue", padx=10, pady=5).pack(pady=5)
tk.Label(root, text="Raised border", relief="raised", bd=3, padx=10).pack(pady=5)
tk.Label(root, text="A long text that wraps after 200 pixels so it stays readable",
         wraplength=200, justify="left").pack(pady=5)
tk.Label(root, text="Fixed width, left aligned", width=30, bg="lightyellow", anchor="w").pack(pady=5)

# Changing a label later
status = tk.Label(root, text="Waiting...", fg="gray")
status.pack(pady=5)
status.config(text="Updated with config()", fg="green")
status["text"] = "Updated with item assignment"
print(status.cget("text"), "|", status["fg"])

# A StringVar linked to a label: change the variable and the label follows
var = tk.StringVar(value="From a StringVar")
tk.Label(root, textvariable=var).pack()
var.set("The StringVar changed")
print(var.get())

# Trap: pack() returns None
wrong = tk.Label(root, text="trap").pack()
print("wrong is", wrong)
right = tk.Label(root, text="correct")
right.pack()
print("right is", type(right).__name__)

root.mainloop()