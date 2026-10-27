class Student:
    school = "Ducat"                   # class attribute: shared
    count = 0                          # a shared counter

    def __init__(self, name):
        self.name = name               # instance attribute: one per object
        Student.count += 1

s1 = Student("Asha")
s2 = Student("Ravi")
print(Student.count, s1.count, s2.count)
print(Student.school, s1.school, s2.school)

# Assigning through an instance creates an instance attribute that SHADOWS the class one
s1.school = "Other"
print(Student.school, s1.school, s2.school)
print(s1.__dict__, s2.__dict__)
del s1.school
print(s1.school)                       # back to the class attribute

# Changing the class attribute affects every object that has not shadowed it
Student.school = "New Name"
print(s1.school, s2.school)

# Lookup order: the instance first, then the class
print("school" in vars(s1), "school" in vars(Student))

# The += trap: this creates an instance attribute instead of changing the class one
class Counter:
    n = 0
    def bump(self):
        self.n += 1

c = Counter()
c.bump()
c.bump()
print(c.n, Counter.n)

# The shared mutable class attribute trap
class Team:
    members = []                       # shared by every Team!
    def add(self, name):
        self.members.append(name)

t1, t2 = Team(), Team()
t1.add("Asha")
print(t2.members)

class TeamFixed:
    def __init__(self):
        self.members = []              # one list per object
    def add(self, name):
        self.members.append(name)

f1, f2 = TeamFixed(), TeamFixed()
f1.add("Asha")
print(f2.members)