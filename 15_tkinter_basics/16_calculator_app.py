import operator
import tkinter as tk

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        tk.Label(self, text="First").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.first = tk.Entry(self, width=14, justify="right")
        self.first.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

        tk.Label(self, text="Second").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.second = tk.Entry(self, width=14, justify="right")
        self.second.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

        for col, symbol in enumerate(OPS, start=1):
            tk.Button(self, text=symbol, width=3,
                      command=lambda s=symbol: self.calculate(s)).grid(row=2, column=col, padx=2, pady=5)

        self.result = tk.Label(self, text="Result:", font=("Arial", 12), anchor="w")
        self.result.grid(row=3, column=0, columnspan=5, sticky="ew", padx=5, pady=5)
        self.first.focus()

    def calculate(self, symbol):
        try:
            value = OPS[symbol](float(self.first.get()), float(self.second.get()))
        except ValueError:
            self.result.config(text="Please enter two numbers", fg="red")
        except ZeroDivisionError:
            self.result.config(text="Cannot divide by zero", fg="red")
        else:
            self.result.config(text=f"Result: {value:g}", fg="black")

if __name__ == "__main__":
    Calculator().mainloop()