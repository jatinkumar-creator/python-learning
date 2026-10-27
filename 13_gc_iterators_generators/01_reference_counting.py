import sys

a = []
print(sys.getrefcount(a))      # 2: the name 'a' plus the temporary argument to getrefcount
b = a                          # another name for the same object
print(sys.getrefcount(a))
c = [a, a]                     # a list holding it twice
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))
c.clear()
print(sys.getrefcount(a))

# Names are labels, not boxes
x = [1, 2]
y = x
print(x is y, id(x) == id(y))
y.append(3)
print(x)
y = [9]                        # rebinding y does not touch the list x still holds
print(x, y)

# Small ints and interned strings are shared objects
print(sys.getrefcount(0) > 100)
print(id(256) == id(256), "hello" is "hello")    # a SyntaxWarning may appear: that is the point