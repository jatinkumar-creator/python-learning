def parse_int(text, low=None, high=None):
    try:
        value = int(text.strip())
    except ValueError:
        raise ValueError(f"{text!r} is not a whole number") from None
    if low is not None and value < low:
        raise ValueError(f"must be at least {low}")
    if high is not None and value > high:
        raise ValueError(f"must be at most {high}")
    return value

def read_int(prompt, low=None, high=None):
    while True:
        try:
            return parse_int(input(prompt), low, high)
        except ValueError as e:
            print("  Invalid:", e)
        except (EOFError, KeyboardInterrupt):
            print("\n  Input cancelled.")
            raise SystemExit(1)

for text in ("42", " 7 ", "abc", "3.5", "-4", "150"):
    try:
        print(repr(text), "->", parse_int(text, 0, 100))
    except ValueError as e:
        print(repr(text), "-> ValueError:", e)

age = read_int("Enter your age (0-120): ", 0, 120)
print("Next year you will be", age + 1)