a = [1, "hello", True, False]
a.sort()
print(a, "sorted")

a.sort(reverse = "True")
print(a, "sorted and reversed")

a.reverse()
print(a, "just reversed")

b = a.copy()
b = list(a)
b = a[:]
print(b)