def unique_value(a):
    b = []
    for el in a:
        if el not in b: b.append(el)
    print(b)
list = [1, 1, 3, 3, 2, 2, 2, 4, 5, 9, 9]

unique_value(list)