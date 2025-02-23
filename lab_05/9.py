import re

with open("C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_05/row1.txt", encoding="utf-8") as f:
    data = f.read()

modified_text = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
print(modified_text)