# instance method : instance method - first parameter is self , * can access instance data * can access class data. typeical use when work with  object.

# class method : * first parameter cls * cannot access object data * can access class data.
# static method : connot access object or class data . 

class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # instance method
    def drive(self):
        return f"{self.color} {self.brand} is driving and have {self.wheels}!"
    
    #class method 
    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number
        return f"All cars now have {cls.wheels} wheels."
    
    #static method
    @staticmethod
    def car_info():
        return "Cars are a means of transport."
    
##1. Instance Method → drive:

# car1 = Car("Toyota", "Red")

# print(car1.drive())

##2. Class Method → change_wheels:

# print(Car.change_wheels(7))
# print(Car.wheels)

##3. Static Method → car_info

print(Car.car_info())


