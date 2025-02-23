import re

with open("C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_05/row1.txt", encoding="utf-8") as f:
    data = f.read()

snake_case_words = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", data)

def snake_to_camel(snake_str):
    parts = snake_str.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

camel_case_words = [snake_to_camel(word) for word in snake_case_words]

print(camel_case_words)