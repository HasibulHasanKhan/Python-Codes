# print(isinstance(10, object))
# print(isinstance("hello", object))
# print(isinstance(len, object))

class Car:
    wheels = 4

## __init__ : use for initailizing attributes.

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self, speed):
        return f"{self.color} {self.brand} is driving at {speed}km/h!"


car1 = Car("Toyota", "Red")
print(car1.brand)
print(car1.drive(70))

