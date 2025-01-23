a = [1, "hello", True, False]
print(a)
print(len(a))
print(type(a))
print(a[0])
print(a[1:4])
a[2] = 999
a.append(True)
a.insert(0, 123)
a.remove("hello")
a.pop()
a.pop(0)
del a[0]