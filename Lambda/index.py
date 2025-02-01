x = lambda a: a + 12

print(x(7))

# take more value :

x = lambda a, b, c: a + b + c
print(x(5,7,12))

#  lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(7)
print(mydoubler(12))

def myfunc2 (n):
    return lambda a : a * n 
mydoubler2 = myfunc2(2)
mydoubler3 = myfunc2(3)
print(mydoubler2(11))
print(mydoubler2(11))