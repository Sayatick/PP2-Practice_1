def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(str(item) + '\n')
    print(f"List successfully written to '{file_path}'.")
    with open(file_path, 'r') as file:
        print(file.read())

data = ["Hello, World!", "Now I am doing LAB_06"]
file_path = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06/a.txt'

write_list_to_file(file_path, data)