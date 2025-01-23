set = {1, 2, 2, 5, 4}

set2 = {'hello', True}
set2.update(set)
print(set2)

set2.remove(True) # give an error if set is empty
set2.discard(2) # don't give an error if set is empty
set2.pop()
set2.clear()
del set2 
print(set2)