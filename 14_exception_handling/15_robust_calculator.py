import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul,
       "/": operator.truediv, "**": operator.pow}

def calculate(text):
    parts = text.split()
    if len(parts) != 3:
        raise ValueError("use the form: number operator number")
    a, op, b = parts
    if op not in OPS:
        raise ValueError(f"unknown operator {op!r}")
    try:
        return OPS[op](float(a), float(b))
    except ZeroDivisionError:
        raise ZeroDivisionError("cannot divide by zero") from None
    except OverflowError:
        raise ValueError("result is too large") from None

while True:
    text = input("calc> ").strip()
    if text.lower() in {"q", "quit"}:
        break
    try:
        print(calculate(text))
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)