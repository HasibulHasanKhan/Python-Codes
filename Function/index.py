def my_function (fname, lname):
    print(fname +" "+ lname)
my_function("Email", "Refsnes")

#IF we don't no many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function2(*kids):
    print("The youngest child is " + kids[2])

my_function2("Emil", "Tobias", "Linus")

# Passing a list as an Argument :

def my_function3(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function3(fruits)
   
# return value
def my_function4(x):
    return 4 * x
print(my_function4(5))

# to get positional argument use , and /
def my_function(x, /):
  print(x)

my_function(x = 3)

# Recursion :

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Output: ")
tri_recursion(6)   
