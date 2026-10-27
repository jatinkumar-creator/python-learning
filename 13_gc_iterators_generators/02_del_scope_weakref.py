import weakref

class Noisy:
    def __init__(self, name):
        self.name = name
        print(f"{name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

# 1. Destroyed when the LAST reference goes away
x = Noisy("A")
y = x
del x
print("after del x: y still holds it")
del y
print("after del y")

# 2. Rebinding a name drops a reference
n = Noisy("B")
n = Noisy("C")                 # B is destroyed right here
print("after rebinding")

# 3. A local variable dies when the function returns
def make():
    temp = Noisy("temp")
    print("inside the function")

make()
print("after the function")

# 4. An object kept alive by a container
holder = [Noisy("in-list")]
print("list created")
holder.clear()
print("list cleared")

# 5. Weak references do not keep an object alive
class Thing:
    pass

t = Thing()
w = weakref.ref(t)
print(w() is t)
del t
print(w())                     # None: the object is gone

# A cache that never keeps objects alive
cache = weakref.WeakValueDictionary()
obj = Thing()
cache["k"] = obj
print("k" in cache)
del obj
print("k" in cache)

print("end of script (C is destroyed when Python exits)")