def all_elements_true(tup):
    return all(tup)

tup1 = (True, 1, "Hello", 5)
tup2 = (True, 0, "Hello", 5)

print(all_elements_true(tup1))
print(all_elements_true(tup2))