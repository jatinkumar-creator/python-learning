import unicodedata

# Code points
print(ord("A"), ord("é"), ord("😀"))
print(chr(65), chr(233), chr(128512))
print("\u0905", "\N{GREEK SMALL LETTER ALPHA}", "\U0001F600")

# str vs bytes
text = "héllo"
data = text.encode("utf-8")
print(data)
print(len(text), len(data))
print(data.decode("utf-8"))

for t in ["hello", "héllo", "नमस्ते", "😀"]:
    print(t, len(t), len(t.encode("utf-8")))

# Wrong encoding
try:
    data.decode("ascii")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
print(data.decode("ascii", errors="backslashreplace"))

# Identical-looking strings that are not equal
a = "\u00e9"                       # one code point
b = "e\u0301"                      # e + combining accent
print(a == b, len(a), len(b))
na = unicodedata.normalize("NFC", a)
nb = unicodedata.normalize("NFC", b)
print(na == nb, len(nb))

# Case-insensitive comparison
print("Straße".lower() == "STRASSE".lower())
print("Straße".casefold() == "STRASSE".casefold())

# Shifting letters with ord/chr
print(chr(ord("a") + 1))