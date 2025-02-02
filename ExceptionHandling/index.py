# try:
#     print(x)
# except NameError:
#     print("Varibale is not defined")
# except:
#     print("Something else went wrong")

# else: 
#     print("There is no error")

# finally:
#   print("The 'try except' is finished")

# x = -1
# if x < 0:
#     raise Exception ("Sorry, no numbers below zero")

x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")