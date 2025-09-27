thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict.pop("model")
thisdict.popitem() # remove random item .
del thisdict["model"]
thisdict.clear()

print(thisdict)