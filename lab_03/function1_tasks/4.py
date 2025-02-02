def filter_numbers(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
def filter_prime(a):
    return [num for num in a if filter_numbers(num)]

a = list(map(int, input("Numbers seperated by space: ").split()))
print(filter_prime(a))