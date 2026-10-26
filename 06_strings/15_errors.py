# s = "hello"
# s[0] = "J"                       # TypeError: strings are immutable

# print("Age: " + 28)              # TypeError

# print("hello"[5])                # IndexError

# print(",".join([1, 2, 3]))       # TypeError: join needs strings

# print("Hello"[1:4:0])            # ValueError: slice step cannot be zero

# print(r"C:\temp\")               # SyntaxError: raw string can't end with one backslash

# print("5" * "3")                 # TypeError

# print("é".encode("ascii"))       # UnicodeEncodeError

# name = "Asha"
# print("Hello {name}")            # logic bug: prints {name} literally