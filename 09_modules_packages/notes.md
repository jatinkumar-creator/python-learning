# Topic 10: Modules, Packages, and pip

## Why modules?
(Reuse, organisation, namespaces, easier testing)

## Script vs module
| | Script | Module |
|---|---|---|
| How it is used | | |
| What __name__ is | | |
| What the __main__ guard does | | |

## Import styles
| Style | Example | Pros | Cons |
|---|---|---|---|
| import x | | | |
| import x as y | | | |
| from x import a | | | |
| from x import * | | | |

## How Python finds a module
(sys.modules, sys.path, the script's folder first, site-packages)

## Standard library modules I used
| Module | What it is for | One function I used |
|---|---|---|

## Package
(What is a package, what does __init__.py do, relative vs absolute imports, __all__, python -m)

## pip
| Command | What it does |
|---|---|

(Why python -m pip? Why requirements.txt? Why is venv/ not committed?)

## Standard vs third-party
(Where each lives, how to install, how to choose a package safely)

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have

erview questions to answer in notes.md
What is a module, and what is a package?
What is the difference between a script and a module?
What does if __name__ == "__main__": do?
What is the difference between import x, from x import y, and from x import *?
How does Python find the module you import?
What happens if you import the same module twice?
What is __init__.py for?
What is the difference between a relative and an absolute import?
What is a circular import, and how do you fix it?
What does pip do, and what is requirements.txt for?
Why use a virtual environment, and why do you run python -m pip?
What happens if you name your file random.py?