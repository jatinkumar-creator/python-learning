# 1
s = "Python"
print(s[1:4], s[-3:], s[::2], s[::-1])

# 2
print("hello"[1], "hello"[-2], "hello"[1:-1], "hello"[::-2])

# 3
s = "abcdef"
print(s[4:1:-1], s[-1:-4:-1], repr(s[1:4:-1]))

# 4
print("ab" * 3, "-" * 5, repr("ab" * 0))

# 5
print("a" "b" + "c" * 2)

# 6
print("xxhixx".strip("x"), "hello".strip("hel"))

# 7
print("banana".find("an"), "banana".rfind("an"), "banana".find("z"), "aaaa".count("aa"))

# 8
print("a,b,,c".split(","), "a b  c".split(), "a b  c".split(" "))

# 9
print("k=v=x".partition("="), "k=v=x".rpartition("="))

# 10
print("it's".title())

# 11
print("abc" < "abd", "Z" < "a", "10" < "9")

# 12
print(len("héllo"), len("héllo".encode("utf-8")), len("😀"), len("😀".encode("utf-8")))

# 13
print(r"a\nb", len(r"a\nb"), len("a\nb"))

# 14
print(f"{3.14159:.2f} {1234567:,} {0.256:.1%} {255:#x} {5:+d}")

# 15
print(f"{'hi':*^9}", f"{42:06}", f"{'hi':<6}|")

# 16
print("-5".isdigit(), "3.5".isdigit(), "²".isdigit(), "²".isdecimal())

# 17
print("7".zfill(3), "-7".zfill(4), "hi".center(6, "*"))

# 18
print("hello".removeprefix("he"), "hello".removesuffix("lo"))