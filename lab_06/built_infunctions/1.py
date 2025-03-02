from functools import reduce

def multiply_list(a):
    return reduce(lambda x, y: x * y, a)

a = [2, 3, 4, 5]
res = multiply_list(a)

print(res)