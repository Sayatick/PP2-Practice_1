def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"Number of lines in '{file_path}': {line_count}")

file_path = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06/a.txt'
count_lines_in_file(file_path)