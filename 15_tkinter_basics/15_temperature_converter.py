import tkinter as tk

root = tk.Tk()
root.title("Temperature converter")
root.resizable(False, False)

celsius = tk.StringVar()
result = tk.StringVar(value="")

def convert():
    try:
        c = float(celsius.get())
    except ValueError:
        result.set("Please enter a number")
        return
    result.set(f"{c:g} °C = {c * 9 / 5 + 32:.1f} °F")

frame = tk.Frame(root, padx=15, pady=15)
frame.grid()

tk.Label(frame, text="Celsius:").grid(row=0, column=0, sticky="e")
entry = tk.Entry(frame, textvariable=celsius, width=10)
entry.grid(row=0, column=1, padx=5)
entry.focus()
tk.Button(frame, text="Convert", command=convert).grid(row=0, column=2)
tk.Label(frame, textvariable=result, font=("Arial", 12), width=24, anchor="w").grid(
    row=1, column=0, columnspan=3, pady=(10, 0))

root.mainloop()