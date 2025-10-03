
age = 12
num = 27
a = 7
b = 11
temperature = 22
user_role = "guest"

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b 
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
access_level = "Full Access" if user_role else "Limited Access"

print(access_level)