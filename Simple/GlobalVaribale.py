# x = "awesome"

# def myfunc():
#     x = "fantastice"
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)

#-----------------------------------------
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

