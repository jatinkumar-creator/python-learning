#Introduction to Python: Study Notes
1. Why Python?
Readable, simple syntax. It reads close to English and uses indentation instead of braces, so you write less code than in Java or C++.
Interpreted and dynamically typed. There is no separate compile step to manage, and you can test ideas quickly in the REPL.
Multi-paradigm. It supports procedural, object-oriented, and functional styles.
Huge standard library (“batteries included”) and a massive third-party ecosystem on PyPI (pandas, NumPy, Django, FastAPI, TensorFlow, PyTorch).
Portable. The same code runs on Windows, Linux, and macOS.
Strong community and job demand, especially in data, AI, automation, and web development.
Trade-off: it is slower than compiled languages for CPU-heavy work, and the GIL limits multi-threaded CPU parallelism in the standard build.
2. History
Year	Milestone
Late 1980s	Guido van Rossum starts Python at CWI, Netherlands, as a successor to the ABC language
1991	First public release (0.9.0)
1994	Python 1.0
2000	Python 2.0 (list comprehensions, garbage collection)
2008	Python 3.0, which was not backward compatible
2020	Python 2 officially end-of-life (2.7 was the last)

The name comes from the comedy group Monty Python’s Flying Circus, not the snake. Python is managed by the Python Software Foundation (PSF). Guido was called the “Benevolent Dictator For Life” until he stepped down in 2018, after which a steering council took over.

3. Application areas
Data science and analytics: pandas, NumPy, Matplotlib
AI/ML and GenAI: scikit-learn, TensorFlow, PyTorch, LangChain
Web development: Django, Flask, FastAPI
Automation and scripting: file handling, DevOps tasks, web scraping
Cybersecurity and digital forensics: scripting, log and artifact parsing, network tools
Scientific computing: SciPy, bioinformatics
Desktop apps and games: Tkinter, PyQt, Pygame
Testing: pytest, Selenium
Embedded and IoT: MicroPython, Raspberry Pi
4. Python implementations

“Python” is a language specification. An implementation is a program that runs it.

Implementation	Written in	Runs on	Key points
CPython	C	Native machine	The reference and default implementation, the one you download from python.org. It has the widest library support (including C extensions).
Jython	Java	JVM	Compiles Python to Java bytecode. Gives direct access to Java libraries. Supports only Python 2.7, with Python 3 support still in development.
IronPython	C#	.NET / CLR	Integrates with .NET libraries. Used for .NET scripting and embedding. It lags behind CPython versions.
PyPy	Python (RPython)	Native machine	Has a JIT (Just-In-Time) compiler, so long-running, CPU-heavy code is often several times faster. It has weaker support for some C-extension libraries.

Others worth knowing: MicroPython (microcontrollers), Cython (compiles Python-like code to C), and Anaconda, which is a distribution (a packaged environment), not an implementation.

5. Python versions
Python 2.x: legacy and unsupported. It had print as a statement and integer division that truncated.
Python 3.x: the present and future. Key differences from 2:
print() is a function
/ always gives true division (use // for floor)
Strings are Unicode by default
range() is lazy, and input() always returns a string
A new minor version is released roughly every year (October), and each is supported for about five years. Recent versions added features such as match statements (3.10), faster interpreters (3.11+), and experimental free-threaded (no-GIL) builds (3.13+). Check python.org for the current stable release before installing.
6. Installing Python
Download the installer from python.org (or use a package manager: apt, brew, winget).
On Windows, tick “Add Python to PATH” during setup.
Verify: python --version (or python3 --version on Linux and macOS), and pip --version.
Use virtual environments per project to isolate dependencies: python -m venv venv, then activate it.
Install packages with pip: pip install requests.
Choose an editor or IDE: VS Code, PyCharm, or Jupyter Notebook.
7. Python interpreter architecture

Python is often called “interpreted,” but CPython actually does both compilation and interpretation:

Source code (.py)
      ↓
 Lexer / Parser → AST
      ↓
 Compiler → Bytecode (.pyc)
      ↓
 Python Virtual Machine (PVM)
      ↓
 Executes on the CPU / OS
Source code is written in a .py file.
Compiler: the source is tokenized, parsed into an Abstract Syntax Tree, and compiled into bytecode. This happens automatically when you run the script, and no manual compile step is needed.
Bytecode: a low-level, platform-independent set of instructions.
PVM: the runtime engine that executes the bytecode.
8. Python bytecode
Bytecode is an intermediate, platform-independent representation of your program. It is not machine code.
It is cached as .pyc files in the __pycache__ folder, so unchanged modules start faster next time. This speeds up loading, not execution.
The same bytecode can run on any OS with a compatible Python version. It is version-specific, though, so 3.11 bytecode won’t run on 3.12.
You can inspect it with the dis module:
python
import dis

def add(a, b):
    return a + b

dis.dis(add)

This prints instructions like LOAD_FAST a, LOAD_FAST b, BINARY_OP, and RETURN_VALUE. The exact names vary by Python version.

9. Python Virtual Machine (PVM)
The PVM is the runtime engine inside the interpreter. It is a loop that reads bytecode instructions one by one and executes them. It is a stack-based machine, because operands are pushed to and popped from a stack.
It handles memory management (reference counting plus a cyclic garbage collector), exceptions, and calls to C extension code.
Modern versions add optimizations such as adaptive specialization of hot instructions (3.11+) and an experimental JIT (3.13+).
GIL (Global Interpreter Lock): in the standard CPython build, only one thread executes Python bytecode at a time. This is fine for I/O-bound tasks, but for CPU-bound work you use multiprocessing or native extensions. Free-threaded builds relax this restriction.