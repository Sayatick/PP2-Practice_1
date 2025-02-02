numbers = [1, 6, 2, 3, 4, 9, 11, -5, -84, 85, 67, 47, 99]

func = lambda num: num > 1 and all(num % i != 0 for i in range(2, num))

prime_list = list(filter(func, numbers))

print(prime_list)