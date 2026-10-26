import py_compile
import pathlib

import helper                     # importing creates helper's .pyc automatically

print(helper.greet("Jatin"))

# Compile explicitly
compiled_path = py_compile.compile("helper.py")
print("Compiled file:", compiled_path)

# List what is inside __pycache__
for f in pathlib.Path("__pycache__").glob("*.pyc"):
    print(f.name, "-", f.stat().st_size, "bytes")