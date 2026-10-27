import gc
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"  {self.name} destroyed")

print("gc enabled:", gc.isenabled())
print("thresholds:", gc.get_threshold())     # commonly (700, 10, 10) on Python 3.12
print("counts    :", gc.get_count())
gc.collect()                                 # start from a clean slate

print("\n--- a reference cycle ---")
a = Node("a")
b = Node("b")
a.other = b
b.other = a
del a, b
print("names deleted, but the two objects still reference each other")
print("collect() found:", gc.collect(), "unreachable objects")

print("\n--- a self-reference ---")
s = Node("self-ref")
s.other = s
del s
print("collect() found:", gc.collect())

print("\n--- breaking the cycle with a weak reference ---")
parent = Node("parent")
child = Node("child")
child.other = weakref.ref(parent)            # does not keep the parent alive
parent.other = child
del parent
print("after del parent: child.other() ->", child.other())
del child

print("\n--- finding objects ---")
print(len(gc.get_objects()) > 1000)
print(gc.get_stats()[0])                     # collection statistics for generation 0

gc.disable()
print("disabled:", not gc.isenabled())
gc.enable()
print("enabled :", gc.isenabled())