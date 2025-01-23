a = [1, "hello", True, False]
for element in a:
    print(element)
    
[print(x) for x in a]

list(map(print, a))