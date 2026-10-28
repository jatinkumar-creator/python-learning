import re

s = "cat bat rat"
print("match      :", re.match(r"cat", s))
print("match 'bat':", re.match(r"bat", s))               # None: match only looks at the START
print("search     :", re.search(r"bat", s))
print("fullmatch  :", re.fullmatch(r"cat", s), re.fullmatch(r"\w+ \w+ \w+", s))
print("findall    :", re.findall(r"[a-z]at", s))
print("finditer   :", [(m.group(), m.span()) for m in re.finditer(r"[a-z]at", s)])

# findall returns different shapes depending on the number of groups
print(re.findall(r"\d+", "1-2 3-4"))                      # no group   -> list of strings
print(re.findall(r"(\d+)", "1-2 3-4"))                    # one group  -> list of that group
print(re.findall(r"(\d+)-(\d+)", "1-2 3-4"))              # two groups -> list of tuples

# Replacing
print(re.sub(r"[aeiou]", "*", "education"))
print(re.sub(r"\s+", " ", "a   b \n c"))
print(re.subn(r"a", "A", "banana"))
print(re.sub(r"a", "A", "banana", count=2))

# Splitting
print(re.split(r"\s*,\s*", "a , b,c ,  d"))
print(re.split(r",", "a,b,c,d", maxsplit=2))
print(re.split(r"\d", "a1b2c3"))                          # note the trailing ''
print(re.split(r"(,)", "a,b"))                            # a capturing group keeps the separators

# Escaping text you want to match literally
print(re.escape("a.b*c"))
print(bool(re.search("a.b", "axb")), bool(re.search(re.escape("a.b"), "axb")))

# Compiled patterns
pat = re.compile(r"\d+")
print(type(pat).__name__, pat.pattern, pat.flags, pat.groups)    # flags 32 means UNICODE is on by default
print(pat.findall("a1 b22"), pat.search("x9").group(), pat.sub("#", "a1 b22"))

# match versus fullmatch versus search for VALIDATION
print(bool(re.match(r"\d+", "123abc")), bool(re.fullmatch(r"\d+", "123abc")))