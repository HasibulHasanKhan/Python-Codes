price = 42
txt = f"The price is {price:.2f} dollars"
print(txt)

txt2 = f"It is very {'Expensive' if price>20 else 'Cheap'}"
print(txt2)
fruit = "apple"
txt3 =f"I love {fruit.upper()}"
print(txt3)

age = 23
name = "John"
txt = "His name is {1} is {0} years old."
print(txt.format(age,name))