def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

N = 5
for el in square_generator(N):
    print(el)