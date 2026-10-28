import re

def show(pattern, text, flags=0):
    print(f"{pattern:<20}{text!r:<28}{re.findall(pattern, text, flags)}")

show(r"\d+", "a1 b22 c333")
show(r"\D+", "a1b22")
show(r"\w+", "Hello, World_42!")
show(r"\W+", "Hello, World_42!")
show(r"\s+", "a b\tc\nd")
show(r"\S+", "a  bb\tccc")

print("\n--- word boundaries ---")
show(r"\bcat\b", "cat concat cat. cats")
show(r"\Bcat", "cat concat")
show(r"\b\w", "hello big world")

print("\n--- \\A and \\Z versus ^ and $ ---")
show(r"^abc", "abc\nabc", re.M)
show(r"\Aabc", "abc\nabc", re.M)
print(bool(re.search(r"abc$", "abc\n")), bool(re.search(r"abc\Z", "abc\n")))   # $ also matches before a final newline

print("\n--- Unicode: \\d and \\w are not just ASCII ---")
digits = "\u0663\u0664 12"                       # two Arabic-Indic digits, a space, then 12
print(len(re.findall(r"\d", digits)), len(re.findall(r"\d", digits, re.A)))
print(re.findall(r"\w+", "über café"), re.findall(r"\w+", "über café", re.A))
print(re.findall(r"[0-9]+", digits))             # [0-9] means ASCII digits only

print("\n--- a readable pattern: the digits of a date ---")
print(re.findall(r"\b\d{4}-\d{2}-\d{2}\b", "from 2026-10-27 to 2026-11-03, not 12026-10-277"))