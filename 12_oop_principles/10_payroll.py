#(inheritance and polymorphism)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r})"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):
        return super().monthly_pay() + self.bonus / 12

class Developer(Employee):
    def __init__(self, name, salary, overtime_hours=0):
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours

    def monthly_pay(self):
        return super().monthly_pay() + self.overtime_hours * 500

staff = [Employee("Ravi", 480000),
         Manager("Meera", 960000, 120000),
         Developer("Asha", 720000, 10)]

for e in staff:
    print(f"{e.name:<8}{type(e).__name__:<11}{e.monthly_pay():>10,.2f}")
print(f"{'Total':<19}{sum(e.monthly_pay() for e in staff):>10,.2f}")
print(max(staff, key=lambda e: e.monthly_pay()))