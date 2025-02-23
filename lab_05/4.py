import re

with open("C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_05/row1.txt", encoding="utf-8") as f:
    data = f.read()

matches = re.findall(r"\b[A-Z][a-z]+\b", data)
print(matches)