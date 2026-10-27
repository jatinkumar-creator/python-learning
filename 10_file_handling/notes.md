# Topic 11: File Handling

## Life cycle of a file
(open, read or write, close; why closing matters)

## Modes
| Mode | Meaning | Erases existing data? | Creates if missing? |
|---|---|---|---|
| r | | | |
| w | | | |
| a | | | |
| x | | | |
| r+ | | | |
| w+ | | | |
| a+ | | | |
| b / t | | | |

## Read and write methods
| Method | What it does | Returns |
|---|---|---|
| read() | | |
| read(n) | | |
| readline() | | |
| readlines() | | |
| for line in f | | |
| write(s) | | |
| writelines(seq) | | |
| seek / tell / truncate / flush / close | | |

## The with block
(What it guarantees. What happens without it.)

## Text vs binary
(When to use each. Encoding, newlines, bytes.)

## pathlib / os / shutil
(Which function for: exists, list, rename, copy, delete, join paths)

## csv and json
(When to use each. What JSON changes. Why newline="" for csv.)

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have

Interview questions to answer in notes.md
What are the steps in handling a file, and why must you close it?
What is the difference between modes r, w, a, and x? Which ones destroy data?
What is the difference between read(), readline(), and readlines()?
How do you read a very large file without loading it all into memory?
What is the with block, and what does it guarantee?
What does seek() do, and what do the three whence values mean?
What is the difference between text mode and binary mode?
Why should you always pass encoding="utf-8" to open()?
What is the difference between write() and writelines()?
What is the difference between a relative path and an absolute path, and why do relative paths cause bugs?
What are csv and json for, and what does json.dumps do to a tuple?
How do you check whether a file exists, delete it, rename it, and copy it?