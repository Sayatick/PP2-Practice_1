def down(n):
    while n >= 0:
        yield n
        n -= 1
        
n = int(input())

for el in down(n):
    print(el)