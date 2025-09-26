# thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
# thislist.sort(reverse=True)
# print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

# def myfunc(n):
#     return abs(n - 50)

# thislist.sort(key = myfunc)

thislist.sort(key = str.lower)

print(thislist)