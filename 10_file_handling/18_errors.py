from common import SCRATCH
p = SCRATCH / "errors.txt"
p.write_text("data", encoding="utf-8")

# open(SCRATCH / "missing.txt")                      # FileNotFoundError

# open(SCRATCH)                                      # PermissionError on Windows (IsADirectoryError on Linux)

# open(p, "x")                                       # FileExistsError

# with open(p) as f:
#     pass
# f.read()                                           # ValueError: I/O operation on closed file

# open(p, "w").read()                                # io.UnsupportedOperation: not readable

# open(p, "w").write(42)                             # TypeError: write() argument must be str

# open(p, "rb").read().decode("ascii")               # fine here, but try non-ASCII data

# (SCRATCH / "bin.dat").write_bytes(b"\xff\xfe\xfd")
# (SCRATCH / "bin.dat").read_text(encoding="utf-8")  # UnicodeDecodeError

# import json
# (SCRATCH / "empty.json").write_text("")
# json.load(open(SCRATCH / "empty.json"))            # JSONDecodeError

# open("C:\new\table.txt")                           # OSError: the path contains a real newline and tab