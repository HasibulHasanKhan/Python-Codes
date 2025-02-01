x = 200
def myfunc():
    global x
    x = 300
myfunc()
print(x)