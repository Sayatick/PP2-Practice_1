import re

with open("C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_05/row1.txt") as f:
    data = f.read()

matches = re.findall(r"\bab*\b", data)
print(matches)