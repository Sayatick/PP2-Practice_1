def histogram(a):
    for el in a:
        for i in range(el):
            print('*', end = "")
        print()

list = [4, 9, 7]

histogram(list)