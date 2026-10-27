from common import SCRATCH

p = SCRATCH / "enc.txt"
text = "नमस्ते café"
p.write_text(text, encoding="utf-8")
raw = p.read_bytes()
print(raw)
print("characters:", len(text), "bytes:", len(raw))

for enc in ("utf-8", "ascii", "latin-1"):
    try:
        print(f"{enc:<8}->", repr(p.read_text(encoding=enc)))
    except UnicodeDecodeError:
        print(f"{enc:<8}-> UnicodeDecodeError")
print(p.read_text(encoding="ascii", errors="replace"))

# Newlines: Windows text mode writes \r\n by default
q = SCRATCH / "newlines.txt"
with open(q, "w", encoding="utf-8") as f:
    f.write("a\nb\n")
print("default    :", q.read_bytes())

with open(q, "w", encoding="utf-8", newline="\n") as f:
    f.write("a\nb\n")
print("newline=\\n :", q.read_bytes())

with open(q, "w", encoding="utf-8", newline="\r\n") as f:
    f.write("a\nb\n")
print("newline=\\r\\n:", q.read_bytes())

with open(q, encoding="utf-8") as f:
    print("read back  :", repr(f.read()))       # translated to \n
with open(q, encoding="utf-8", newline="") as f:
    print("untranslated:", repr(f.read()))

# utf-8-sig adds a BOM, which Excel uses to recognise UTF-8
p.write_text("café", encoding="utf-8-sig")
print(p.read_bytes())