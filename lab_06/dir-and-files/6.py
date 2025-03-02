import string
import os

def func(path):
    for letter in string.ascii_uppercase:
        file_name = os.path.join(path ,f"{letter}.txt")
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}\n")
        print(f"Created: {file_name}")

dir = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06'
func(dir)