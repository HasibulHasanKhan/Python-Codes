cars = ["Ford", 12, "Volvo", "BMW"]
print(cars)

x = len(cars)

print(x)


# for loop into array :
for x in cars:
    print(x)

cars.append("Honda")

# remove element :
cars.pop(1)
cars.remove("Volvo")

# cars.clear()
# cars.copy()
cars.count("Honda")

#cars.index("Honda"
# insert element by replacing spacific element.

cars.insert(1, "Hasib")
print(cars)
fruits = ['apple', 'banana', 'cherry']

fruits.extend(cars)
print(fruits)
#fruits.remove("Honda")
fruits.reverse()
fruits.sort()
print(fruits)