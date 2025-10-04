# from functools import reduce

def add(x, y):
    return x + y

prices = [19.99, 1.00, 5,75, 10.99]

total = reduce(add, prices)
print(f"${total}")