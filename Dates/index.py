import datetime

x = datetime.datetime.now()
print(x)

c = x.year
d = x.strftime("%A")
print(c)
print(d)

# e = datetime.datetime(2020, 4, 17)
# print(e)


f = x.strftime("%B")
print(f)


g = x.strftime("%d-%m-%Y")
print(g)