a = 1
b = 2

if a > b:
    print(a, "is bigger than ", b)
elif a < b:
    print(a, "is less than ", b)
else:
    print("they are equal")
    
print("A") if a > b else print("=") if a == b else print("B")