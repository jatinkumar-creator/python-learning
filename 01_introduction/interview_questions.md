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

23. Is bytecode the same as machine code?
No. Machine code runs directly on the CPU, while bytecode needs the PVM to interpret it. That extra layer is what makes Python portable.

24. Python is dynamically typed. Is it also weakly typed?
No. It is dynamically and strongly typed: types are checked at runtime, and "5" + 5 raises a TypeError instead of silently converting.