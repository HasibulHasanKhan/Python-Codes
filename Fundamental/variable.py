# global and local variabl :

# x = "Hasib" # global

# def myfunc():
#     x = "Hasan" # local
#     print("Python is: " + x)

# myfunc()
# print("Python is: " + x)

# global keyword 
"""
inside function the local variabe can be global by using of global keyword.

Note : also to change the global varaible inside a function, refer to the variable by using the global keyword.
"""

def myfunc2() :

    global txt
    txt = " Hasibul "

myfunc2()
print("Python is: " + txt)