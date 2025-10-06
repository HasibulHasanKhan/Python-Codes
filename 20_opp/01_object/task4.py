#### Can access and modify class attributes but cannot access instance attributes directly. 
#example :: 

class Car:
    wheels = 2

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @classmethod
    def show_car_info(cls, car_obj):
        return f"{car_obj.color} {car_obj.brand} with {cls.wheels} wheels."
    


car1 = Car("Toyota", "Red")

print(Car.show_car_info(car1))