#global keyword to create a global variable inside function.

def myfunc():
    global x
    x = "Bangladesh"

myfunc()
print("Our country is: " + x)  