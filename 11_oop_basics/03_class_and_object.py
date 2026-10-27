class Empty:
    pass

e1 = Empty()                          # creating an object ("instantiation")
e2 = Empty()

print(type(e1), type(Empty), isinstance(e1, Empty))
print(e1 == e2, e1 is e2, id(e1) == id(e2))     # two separate objects
e1.color = "red"                      # attributes can be added to one object dynamically
print(e1.__dict__, e2.__dict__)
try:
    print(e2.color)
except AttributeError as e:
    print("AttributeError:", e)

print(Empty.__name__, e1.__class__ is Empty)
print(e1)                             # the default text: class name and memory address
print(hasattr(e1, "color"), hasattr(e2, "color"), getattr(e1, "color"), getattr(e2, "color", "none"))
setattr(e2, "color", "blue")
delattr(e1, "color")
print(vars(e1), vars(e2))

print(isinstance(e1, object), isinstance(5, object), type(Empty) is type)