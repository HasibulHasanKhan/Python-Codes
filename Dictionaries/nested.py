# myfamily = {
#     "child1": {
#         "name": "Hasib",
#         "year": 2024
#     },
#     "child2": {
#         "name": "Tobies",
#         "year": 2021
#     },
#     "child3": {
#         "name": "Emon",
#         "year": 2000
#     }
# }
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



# print(myfamily["child1"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])