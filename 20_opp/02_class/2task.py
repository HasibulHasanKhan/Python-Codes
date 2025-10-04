
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    def __str__(self):
        return f"{self.name}({self.age})"
    

p1 = Person("John", 37)

print(p1.myfunc())