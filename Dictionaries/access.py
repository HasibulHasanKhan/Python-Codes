thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# x = thisdict["model"]
# y = thisdict.get("model")
# z = thisdict.keys()
# thisdict["color"] = "white"
# a = thisdict.values()

# b = thisdict.items()

thisdict.update({"year": 2000})

print(thisdict)


# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary.")