import re

print(re.findall(r"\d+(?= dollars)", "10 dollars 20 euros 30 dollars"))      # ['10', '30']
print(re.findall(r"\b\d+\b(?! dollars)", "10 dollars 20 euros 30 dollars"))  # ['20']
print(re.findall(r"(?<=\$)\d+", "cost $50 and 70 and $9"))                   # ['50', '9']
print(re.findall(r"(?<!\$)\b\d+", "$50 and 70 and $9"))                      # ['70']

# The digits are NOT part of the lookaround's match
m = re.search(r"(?<=\$)\d+", "price $250")
print(m.group(), m.span())

# Insert thousands separators with a lookahead
print(re.sub(r"\B(?=(?:\d{3})+$)", ",", "1234567"))                            # 1,234,567

# Password rules: several lookaheads at one position
STRONG = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}")
for pwd in ("abc", "Password1", "P@ssw0rd!", "p@ssw0rd!!"):
    print(f"{pwd:<12}{bool(STRONG.fullmatch(pwd))}")

# Inline flags
print(re.findall(r"(?i)python", "Python PYTHON"))
print(re.findall(r"(?i:py)thon", "PYthon PYTHON"))

# A lookbehind must have a fixed width
try:
    re.compile(r"(?<=a+)b")
except re.error as e:
    print("re.error:", e)