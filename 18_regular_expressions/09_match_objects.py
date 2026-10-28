import re

m = re.search(r"(?P<user>[\w.]+)@(?P<host>[\w.]+)", "mail: asha.k@example.com now")
print(m)
print(m.string, "|", m.re.pattern, "|", m.pos, m.endpos, m.lastindex, m.lastgroup)
print(m.span("user"), m.start("host"), m.end("host"))
print(m.expand(r"\g<user> at \g<host>"))
print(m.groups("-"), bool(m))

pat = re.compile(r"\d+")
print(pat.match("a1", 1).group(), pat.search("a1b22", 2).group(), pat.fullmatch("123") is not None)
print(pat.findall("a1b22c333", 3), pat.sub("#", "a1 b22", count=1), pat.split("a1b22c"))

# The most common bug: calling .group() on None
try:
    re.search(r"\d", "abc").group()
except AttributeError as e:
    print("AttributeError:", e)

# Safe idioms
if m := re.search(r"\d+", "order 66"):
    print("found", m.group())

result = re.search(r"\d+", "no digits")
print(result.group() if result else "no match")

# Looping over every match with positions
for hit in re.finditer(r"\b\w{5}\b", "these words have five and seven letters"):
    print(hit.span(), hit.group())