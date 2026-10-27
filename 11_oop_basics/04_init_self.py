class Student:
    def __init__(self, name, marks=None):
        print(f"__init__ running for {name}")
        self.name = name
        self.marks = marks if marks is not None else []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def whoami(self):
        return self

    def __str__(self):
        return f"{self.name} (avg {self.average():.1f})"

s1 = Student("Asha", [80, 90])
s2 = Student(name="Ravi")             # keyword arguments work too
s2.add_mark(70)
s2.add_mark(95)
print(s1, "|", s2)
print(s1.marks, s2.marks)             # each object has its own list

print(s1.whoami() is s1)              # self IS the object
print(Student.average(s1), s1.average())   # the same call written two ways
print(s1.__dict__)

# The mutable default trap, avoided above with "marks=None"
class Bad:
    def __init__(self, tags=[]):
        self.tags = tags

x, y = Bad(), Bad()
x.tags.append("shared!")
print(y.tags)