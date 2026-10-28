import re

text = "Python python PYTHON\nsecond line\nthird"
print(re.findall(r"python", text), re.findall(r"python", text, re.I))
print(re.findall(r"^\w+", text, re.M))
print(re.findall(r"line.third", text), re.findall(r"line.third", text, re.S))
print(re.findall(r"^p\w+", text, re.I | re.M))
print({f.name: int(f) for f in (re.I, re.M, re.S, re.X, re.A, re.U)})

# Verbose mode: whitespace and comments make a big pattern readable
PHONE = re.compile(r"""
    \(?(\d{3})\)?      # area code, with optional parentheses
    [\s.-]?            # an optional separator
    (\d{3})            # exchange
    [\s.-]?
    (\d{4})            # line number
""", re.X)
print(PHONE.findall("(555) 123-4567, 555.987.6543, 5551112222"))

# Inside a character class, whitespace and # still count as themselves
print(re.findall(r"""[ #]+""", "a # b", re.X))

# Build a big pattern from named pieces
YEAR = r"\d{4}"
MONTH = r"(?:0[1-9]|1[0-2])"
DAY = r"(?:0[1-9]|[12]\d|3[01])"
DATE = re.compile(rf"\b{YEAR}-{MONTH}-{DAY}\b")
print(DATE.findall("2026-10-27, 2026-13-01, 2026-02-31"))