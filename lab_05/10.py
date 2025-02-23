import re

with open("C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_05/row1.txt", encoding="utf-8") as f:
    data = f.read()
    
def camel_to_snake(text):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", text).lower()

s = "convertThisString"
print(camel_to_snake(s))