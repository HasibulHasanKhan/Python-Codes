#Lists are used to store multiple items in a single varible.

#store same value also.
#also contain different data types.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

list1 = ["hasib", 34, True, "hasan"]

a = len(thislist)
print(a)


b = type(thislist)
print(b)

# list() constructor to make a list :

list2 = (("mango", 44, True))
#access list item :

c = thislist[1]
d = thislist[-1] # -1 refers to the item is last .

# range of indexes : 
e = thislist[2:7]
print(e)

#check item :
if "apple" in thislist:
    print("yes, 'apple' is in the fruits list")
# change range of item value and insert more item by moving remaining item.

thislist[1:3] = ["blackcurrant", "watermenlin"]
print(thislist)

#insert items :
thislist.insert(2, "pineal")