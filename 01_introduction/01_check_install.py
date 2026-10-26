import platform
import sys

print("Python version     :", platform.python_version())
print("Implementation     :", platform.python_implementation())   # CPython, PyPy, ...
print("Compiler used      :", platform.python_compiler())
print("Executable path    :", sys.executable)
print("OS                 :", platform.system(), platform.release())
print("Version info tuple :", sys.version_info)
print("Is Python 3?       :", sys.version_info.major == 3)