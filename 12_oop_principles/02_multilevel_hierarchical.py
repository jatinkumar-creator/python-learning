class Vehicle:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"{self.brand} with {self.wheels} wheels"

class Car(Vehicle):                        # multilevel: Vehicle -> Car -> SportsCar
    def honk(self):
        return "Beep"

class SportsCar(Car):
    def __init__(self, brand, top_speed):
        super().__init__(brand)
        self.top_speed = top_speed

    def info(self):
        return super().info() + f", top speed {self.top_speed}"

class Bike(Vehicle):                       # hierarchical: Car and Bike share a parent
    wheels = 2

sc = SportsCar("Ferrari", 320)
print(sc.info())
print(sc.honk())
print(Bike("Hero").info())
print(SportsCar.wheels, Bike.wheels, Vehicle.wheels)
print([c.__name__ for c in SportsCar.__mro__])
print(Vehicle.__subclasses__())
print(hasattr(sc, "honk"), hasattr(Bike("Hero"), "honk"))