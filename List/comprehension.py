fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for item in fruits:
#     if "a" in item:
#         newlist.append(item)

newlist = [x for x in fruits if "a" in x]

print(newlist)