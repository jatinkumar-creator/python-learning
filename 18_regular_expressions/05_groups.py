import re

m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2026-10-27.")
print(m.group(), m.group(0), m.group(1), m.group(1, 3), m.groups())
print(m.span(), m.span(2), m.start(), m.end())
year, month, day = m.groups()
print(int(year), int(month), int(day))

print("\n--- named groups ---")
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "Date: 2026-10-27.")
print(m.group("year"), m["month"], m.groupdict(), dict(m.re.groupindex))

print("\n--- groups that did not take part ---")
m = re.match(r"(a)(b)?(c)?", "ac")
print(m.groups(), m.groups("-"), m.group(2), m.lastindex)

print("\n--- backreferences: the same text again ---")
print([m.group() for m in re.finditer(r"(\w)\1", "balloon coffee")])
print(re.findall(r"\b(\w+) \1\b", "this is is a test test of the the system"))
print(re.search(r"""(?P<q>["']).*?(?P=q)""", """say "it's ok" now""").group())

print("\n--- groups in replacements ---")
print(re.sub(r"(\w+) (\w+)", r"\2 \1", "hello world"))
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2026-10-27"))
print(re.sub(r"(\d)", r"\g<1>0", "123"))

print("\n--- repeating a group ---")
print(re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", "192.168.1.1") is not None)
print(re.findall(r"(?:ab)+", "ababab ab a"))
print(re.findall(r"(ab)+", "ababab ab a"))             # a repeated group captures only its LAST repetition