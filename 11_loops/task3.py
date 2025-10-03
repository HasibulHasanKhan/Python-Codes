num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10: 
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")