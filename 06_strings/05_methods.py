# Case
s = "hello World"
print(s.upper(), s.lower(), s.title(), s.capitalize(), s.swapcase())

# Searching and counting
t = "banana"
print(t.find("an"), t.rfind("an"), t.find("z"), t.count("a"))
print(t.index("an"), t.startswith("ba"), t.endswith("na"), "nan" in t)
print(t.startswith(("x", "b")))

# Trimming and padding
print("|" + "  hi  ".strip() + "|")
print("xxhixx".strip("x"))
print("hello".removeprefix("he"), "hello".removesuffix("lo"))
print("7".zfill(3), "hi".center(10, "*"), "hi".ljust(5, "."), "hi".rjust(5, "."))

# Splitting and joining
print("a b  c".split())
print("a,b,,c".split(","))
print("a,b,c".split(",", 1))
print("l1\nl2\r\nl3".splitlines())
print("k=v=x".partition("="))
print("-".join(["a", "b", "c"]))
print(",".join(str(n) for n in [1, 2, 3]))

# Replacing and translating
print("hello".replace("l", "L"), "hello".replace("l", "L", 1))
print("Programming".translate(str.maketrans("", "", "aeiou")))

# Testing
print("abc".isalpha(), "abc1".isalnum(), "".isalpha(), "12".isdigit())
print("-5".isdigit(), "3.5".isdigit())
print("²".isdigit(), "²".isdecimal(), "½".isnumeric())
print("   ".isspace(), "ABC".isupper(), "abc".islower())

# Sorting characters
print(sorted("cab"), "".join(sorted("cab")))