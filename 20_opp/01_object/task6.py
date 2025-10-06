# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name}"
    
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


#     def display_age(self):
#         return f"I am {self.age} years old."
    
    
# c = Child("Hasib", 22)
# print(c.greet())
# print(c.display_age)

## override a method : 


# class Parent:
#     def greet(self):
#         return "I am from parent."
    
# class Child:
#     def greet(self):
#         return "I am form child."

# c = Child()
# print(c.greet())

## using super() for Method overring :

class Parent:
    def greet(self):
        return "I am form parent"
    
class Child(Parent):
    def greet(self):
        parent_msg = super().greet()
        return(f"{parent_msg} and Hello from Child.")
    
c = Child()
print(c.greet())
