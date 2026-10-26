name = "Jatin"
age = 28
pi = 3.14159

print("Name:", name, "Age:", age)            # comma-separated
print(f"Name: {name}, Age: {age}")           # f-string (preferred)
print("Name: {}, Age: {}".format(name, age)) # str.format()
print("Name: %s, Age: %d" % (name, age))     # old % style
print(f"{pi:.2f}")                           # 2 decimal places
print(f"{age=}")                             # debug style
print("""This text
spans three
lines""")