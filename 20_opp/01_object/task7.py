## Method Overriding :

## Method Overriding happens when a child class provides its own implementation of a method already defined in the parent class.

## It allows polymorphism (same method behaves differently depending on the object).

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Overrides parent method
        return "Hello from Child"

c = Child()
print(c.greet())  # Output: Hello from Child

## Key Points for Overriding:
## Same method name and parameters as in the parent.
## Child method replaces the parent method for child objects.
## Can use super() to call the parent’s method if needed.

class Child(Parent):
    def greet(self):
        parent_msg = super().greet()
        return f"{parent_msg} and Hello from Child"
    

# Method Overloading :

# Definition:
# Method Overloading is having multiple methods with the same name but different parameters (number or type of parameters) in the same class.

# Python does NOT support traditional method overloading like Java or C++.
# But we can achieve it using:
# Default arguments
# *args or **kwargs