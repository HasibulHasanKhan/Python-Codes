a = 21
b = 23
if b < a:
    print("b is less than a")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

# multiple statements on the same llne:

a = 330
b = 333
c = 334
print("A") if a > b else print("=") if a == b else print("b")
# and | or | not 
if  a > b and c > a:
    print("Both conditions are True")

if not a > b:
    print ("a is NOT greater than b")

x = 423
if x > 29:
    print("Above ten")

    if x > 44:
        print("Above 40")
        if b > a:
             pass