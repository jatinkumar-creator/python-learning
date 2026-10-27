import importlib
import sys

import mathutils

print("Folder of this script:", sys.path[0])
for p in sys.path[:5]:
    print(" ", p)

print("mathutils" in sys.modules)
importlib.reload(mathutils)        # re-runs the module's top-level code
print(sys.modules["mathutils"] is mathutils)

print(sys.prefix)
print(sys.base_prefix)
print("Inside a venv:", sys.prefix != sys.base_prefix)
print(sys.executable)
print(sys.argv)