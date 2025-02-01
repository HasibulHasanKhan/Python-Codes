"""
A for loop is used for iterating over a sequence (that is either a list , a tuple, a dictionary, a set or a string)
"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
# looping through string :


for x in "Banana":
   
    if x == "n":
     break
    print(x) # B and a 

for x in "Banana":
       print(x)
       if x == "n": # B and a  and n
        break

# range :
for x in range(7, 344 ,7):
   print(x)

# Nested loop : The inner loop will be executed one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
   for y in fruits:
      print(x, y)