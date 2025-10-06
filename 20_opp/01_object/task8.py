# Method Overloading : 

# Definition:
# Method Overloading is having multiple methods with the same name but different parameters (number or type of parameters) in the same class.

# Python does NOT support traditional method overloading like Java or C++.
# But we can achieve it using:
# Default arguments
# *args or **kwargs

# class Math:
#     def add(self, a, b = 2):
#         return a + b
    

# m = Math()

# print(m.add(5))
# print(m.add(5, 11))
    

## using with args :

class Math:
    def add(self, *args):
        return sum(args)
    

m = Math()
print(m.add(5))
print(m.add(5,12))
print(m.add(2,5,6,7))
