# The self parameter is a reference to the current instance of the class , and is used to access variable that belongs to the class.

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = Person("John", 27)
print(p1.name)
print(p1.age)
          

class People:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   def __str__(self):
      return f"{self.name} ({self.age})"
p2 = Person("John", 37)
print(p2.age)