list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# for item in list2:
#     list1.append(item)

list1.extend(list2)

print(list1)