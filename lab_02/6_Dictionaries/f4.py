dict = {
  "brand": "Volkswagen",
  "model": "Golf",
  "year": 2001
}

for x in dict:
    print(x, dict[x])\

for x in dict.values():
    print(x)
    
for x in dict.keys():
    print(x)

for x,y in dict.items():
    print(x, y)