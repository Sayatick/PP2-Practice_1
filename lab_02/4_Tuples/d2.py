data = (1, 5, 2, 3, "hello", True)

data_2 = 1, 2, 4, False, "this is also tuple"
print(data_2, "- data 2")

data_3 = ("hello",) #this is tuple with 1 element(comma at the end!)
print(data_3, "- data 3")

list_1 = [1, "aaa"]
data_4 = tuple(list_1)
print(data_4, "- data 4")

data_5 = tuple("word") #divides each letter into one tuple
print(data_5, "- data 5")