import re

print(re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b22 c3"))
print(re.sub(r"\b\w", lambda m: m.group().upper(), "hello big world"))
print(re.sub(r"(?<!^)(?=[A-Z])", "_", "userFirstName").lower())
print(re.sub(r"_([a-z])", lambda m: m.group(1).upper(), "user_first_name"))
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2026-10-27 and 2025-01-05"))
print(re.sub(r"(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})", r"\g<d>.\g<m>.\g<y>", "2026-10-27"))
print(re.sub(r"\d(?=\d{4})", "*", "1234567812345678"))

# A tiny template engine
template = "Hello {{name}}, you owe {{amount}}. {{unknown}} stays."
values = {"name": "Asha", "amount": "Rs. 500"}
print(re.sub(r"\{\{(\w+)\}\}", lambda m: values.get(m.group(1), m.group(0)), template))

# Replacement strings are processed: \n becomes a newline
print(repr(re.sub(r"a", r"\n", "banana")))
print(re.sub(r"a", lambda m: r"\n", "banana"))       # a function's result is used literally

# Count how many replacements happened
cleaned, n = re.subn(r"\s+", " ", "too    many     spaces")
print(repr(cleaned), n)

# A cleaning pipeline
raw = "  Hello,   World!!   It's   2026.  "
step1 = re.sub(r"\s+", " ", raw).strip()
step2 = re.sub(r"[^\w\s']", "", step1)
print(repr(step1), repr(step2), step2.lower().split())