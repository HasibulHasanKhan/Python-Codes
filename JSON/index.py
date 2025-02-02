import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["age"])

a = {
    "name": "Hasib",
    "age": 243,
    "city": "Sylhet"
}

b = json.dumps(a)
print(b)