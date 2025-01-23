dict = {
  "brand": "Volkswagen",
  "model": "Golf",
  "year": 2001
}

print(len(dict))
print(type(dict))

dict["color"] = "red"

dict["year"] = 1999
dict.update({"year":1998})
print(dict)