print(int("42"), int("  42  "), int("-7"), int("1_000"))
print(int("ff", 16), int("1010", 2))
print(int(3.9), int(-3.9))                     # truncates, doesn't round
print(float("3.14"), float("1e3"))
print(round(2.5), round(3.5))                  # banker's rounding

for text in ["3.5", "abc", "12,5", ""]:
    try:
        print(int(text))
    except ValueError as e:
        print(f"int({text!r}) -> ValueError: {e}")

print(bool("False"), bool(""))                 # truthiness of strings
print("-5".isdigit())                          # isdigit is not a number check