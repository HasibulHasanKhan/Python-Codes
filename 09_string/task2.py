username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == - 1:
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}")   