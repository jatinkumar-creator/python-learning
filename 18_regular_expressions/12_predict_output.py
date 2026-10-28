import re

# 1
print(re.match(r"\d+", "abc123"), re.search(r"\d+", "abc123").group())

# 2
print(re.findall(r"a.c", "abc a\nc a c"))

# 3
print(re.findall(r"\d{2,3}", "1 12 123 1234 12345"))

# 4
print(re.findall(r"(a)(b)?", "ab a"))

# 5
print(re.sub(r"(\w+) (\w+)", r"\2 \1", "one two three four"))

# 6
print(re.split(r"\d", "a1b2c3"), re.split(r"(\d)", "a1b2c"))

# 7
print(re.findall(r"<.+>", "<a><b>"), re.findall(r"<.+?>", "<a><b>"))

# 8
print(re.findall(r"^\w+", "a b\nc d"), re.findall(r"^\w+", "a b\nc d", re.M))

# 9
print(bool(re.match(r"abc$", "abc\n")), bool(re.match(r"abc\Z", "abc\n")))

# 10
print(re.findall(r"\bis\b", "this is his island"))

# 11
print(repr(re.sub(r"\s+", " ", "  a   b  ")))

# 12
print(re.fullmatch(r"\d+", "123abc"), bool(re.fullmatch(r"\d+", "123")))

# 13
print(re.findall(r"(?<=\$)\d+", "$5 7 $9"))

# 14
print(re.findall(r"[\w.]+@\w+\.com", "a.b@x.com, c@y.org"))

# 15
m = re.search(r"(?P<k>\w+)=(?P<v>\d+)", "x=1, y=22")
print(m.groupdict(), m.span(), m.end("v"))

# 16
print(re.findall(r"[A-Z][a-z]+", "HelloWorld ABC Python"))

# 17
print(re.findall(r".*", "ab"), re.sub(r"x*", "-", "abc"))

# 18
print(re.escape("1+1"), bool(re.search(re.escape("1+1"), "1+1=2")), bool(re.search("1+1", "1+1=2")))

# 19
print(re.match(r"(a|ab)(c|bcd)(d*)", "abcd").groups())

# 20
print(re.sub(r"a", "X", "AaAa", re.I), re.sub(r"a", "X", "AaAa", flags=re.I))