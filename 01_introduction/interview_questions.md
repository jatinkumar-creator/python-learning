Interview Questions: Introduction to Python
Basic level

1. Why would you choose Python for a project?
It has readable syntax, fast development, a huge standard library and package ecosystem (PyPI), cross-platform portability, and strong community support, especially in data, AI, web, and automation. The trade-off is slower raw execution than compiled languages.

2. Who created Python, and why is it called Python?
Guido van Rossum, who started it in the late 1980s, with the first public release in 1991. The name comes from Monty Python’s Flying Circus, not the snake.

3. Is Python compiled or interpreted?
Both. CPython first compiles source code to bytecode, then the Python Virtual Machine interprets that bytecode. Calling it purely “interpreted” is a common oversimplification.

4. What are the main differences between Python 2 and Python 3?
In Python 3, print is a function, / is true division, strings are Unicode by default, and range() is lazy. Python 2 reached end-of-life in 2020.

5. Name some application areas of Python.
Data science, AI/ML, web development (Django, Flask, FastAPI), automation and scripting, cybersecurity and forensics, scientific computing, testing, and IoT (MicroPython).

6. What is pip, and why use virtual environments?
pip installs packages from PyPI. A virtual environment (python -m venv venv) isolates each project’s dependencies, so different projects can use different package versions without conflict.

Implementations

7. What is the difference between a language and an implementation? Name four Python implementations.
Python is the language specification, and an implementation is a program that runs it. CPython (C, the reference implementation), Jython (JVM), IronPython (.NET), and PyPy (JIT-compiled).

8. Why is PyPy often faster than CPython, and why isn’t it the default?
PyPy has a JIT compiler that optimizes hot code at runtime, which helps long-running, CPU-heavy programs. It isn’t the default because CPython has the broadest compatibility, especially with C-extension libraries, and PyPy’s advantage is smaller on short scripts.

9. When would you use Jython or IronPython?
Jython when you need direct access to Java libraries from Python, and IronPython for .NET integration. Both lag behind CPython versions, so check current compatibility before relying on them.

10. What is the difference between CPython and Cython?
CPython is the standard interpreter. Cython is a tool and language that compiles Python-like code, with optional C type declarations, into C extensions for speed. The names are easy to confuse.

Architecture, bytecode, and PVM

11. Explain what happens when you run a Python script.
The source is tokenized and parsed into an AST, the compiler turns the AST into bytecode, and the PVM executes the bytecode instruction by instruction.

12. What is Python bytecode?
A low-level, platform-independent intermediate representation of your code. It isn’t machine code, and it’s specific to the Python version, so 3.11 bytecode won’t run on 3.12.

13. What is a .pyc file, and does it make code run faster?
It’s cached bytecode stored in __pycache__. It makes loading faster for imported modules, since recompilation is skipped when the source is unchanged. It does not speed up execution.

14. Does running python script.py create a .pyc file for that script?
No. Only imported modules are cached. The top-level script is compiled in memory each time.

15. What is the PVM?
The runtime engine inside the interpreter. It’s a stack-based virtual machine that loops over bytecode instructions, handles memory management, exceptions, and calls into C extensions.

16. How can you inspect bytecode?
With the dis module: import dis; dis.dis(func). It shows instructions like LOAD_FAST and RETURN_VALUE, whose exact names vary by version.

17. What is the GIL, and why does it matter?
The Global Interpreter Lock lets only one thread execute Python bytecode at a time in standard CPython. It’s fine for I/O-bound work, but CPU-bound code needs multiprocessing or native extensions. Recent versions have experimental free-threaded builds that remove this limit, so check the current status.

18. How does Python manage memory?
Mainly reference counting, plus a cyclic garbage collector to handle reference cycles.

Scenario and tricky questions

19. A CPU-heavy Python script is too slow. What are your options?
Profile first (cProfile). Then pick the right fix: better algorithms or data structures, vectorization with NumPy or pandas, multiprocessing, Cython or Numba, a PyPy trial, or rewriting only the hot path in a compiled language.

20. Two projects need different versions of the same library. How do you handle it?
Use a separate virtual environment per project, with pinned versions in requirements.txt or a lock file.

21. After installing Python on Windows, python isn’t recognized. What’s the likely cause?
Python wasn’t added to PATH. Reinstall with “Add Python to PATH” ticked, or add it manually, then verify with python --version.

22. Why can Python be slower than C, despite bytecode?
Dynamic typing means type checks at runtime, bytecode is interpreted instead of run natively, objects carry overhead, and the GIL limits threaded parallelism. Newer versions narrow the gap with specialization and an experimental JIT.


Introduction to Python: Study Notes
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
Quick revision points
Python is a language. CPython, Jython, IronPython, and PyPy are implementations.
Python code is first compiled to bytecode, then interpreted by the PVM.
.pyc files hold cached bytecode and make loading faster, not running.
PyPy is faster because of its JIT, Jython targets the JVM, and IronPython targets .NET.
Python 3 is current, and Python 2 is dead.
Likely exam/interview questions
Is Python compiled or interpreted? (Both: compiled to bytecode, then interpreted by the PVM.)
What is the difference between CPython and PyPy?
What is a .pyc file?
What does the PVM do?
What is the GIL, and why does it matter?

24. Is bytecode the same as machine code?
No. Machine code runs directly on the CPU, while bytecode needs the PVM to interpret it. That extra layer is what makes Python portable.

25. Python is dynamically typed. Is it also weakly typed?
No. It is dynamically and strongly typed: types are checked at runtime, and "5" + 5 raises a TypeError instead of silently converting.
