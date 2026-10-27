import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(r={self.radius})"

class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height})"

shapes = [Circle(1), Rectangle(3, 4), Circle(2), Rectangle(1, 1)]
for s in sorted(shapes, key=lambda s: s.area()):
    print(f"{s!r:<18}area={s.area():>7.2f}  perimeter={s.perimeter():>7.2f}")

print("Largest:", max(shapes, key=lambda s: s.area()))
print("Total area:", round(sum(s.area() for s in shapes), 2))