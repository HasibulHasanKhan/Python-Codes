# name = input("Enter your full name: ")
phone_number = input("Enter your phone num: ")

# result = len(name)
# result = name.rfind("i") #reverse - last occurance
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result2 = name.isalpha() ## space | digit will give err.
# phone_number = phone_number.count("-")
phone_number_replaec = phone_number.replace("-", " ") ## "" remove space.

# print(name)
print(phone_number_replaec)
# print(result) # -1 if no result