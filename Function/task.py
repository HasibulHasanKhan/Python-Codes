# def myFunc(fname, lname):
#     print(fname + " " + lname)

# myFunc("Hasibul", "Hasan")

## arbitary arguments :

# def myFunc2(*kids):
#     print("The youngest child is " +  kids[2])

# myFunc2("Hasib", "Hasan", "Emon")

## Keyword Arguments :
# def myFunc3(child1,child2,child3):
#     print("The youngest child is " + child2)

# myFunc3(child1 = "Hasib" , child2 = "Hasan", child3 = "Emon")

## Arbitary Keyword Arguments, **kwargs:

# def myFunc4(**kid):
#     print("His last name is " + kid["lname"])

# myFunc4(fname = "Tobias", lname = "Refsnes")

##default value as a prarameter :

# def myFunc5(country = "Norway"):
#     print("I am from " + country)

# myFunc5("Sweden")
# myFunc5("Bangladesh")
# myFunc5("England")

## Pasing list as a parameter :
# def myFunc6(food):
#     for x in food:
#         print(x)

# fruits = [1,25,5,5,21,22]
# myFunc6(fruits)

## Pass :
# def myFunc7():
#     pass

## , / are used to allowed to positional argument.

## * used for only keyword argument .
# def myFun8(*, x):
#     print(x)
# myFun8( x = 7)

## Combine Positional Only and Kewword Only.

# def myFunc9(a, b, /, *, c, d):
#     print(a + b + c + d)

# myFunc9(5, 6, c = 7, d = 8)

## Recursion .

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0 
    return result

print("Recursion Example Results:")
tri_recursion(7)