def copy_file_manual(source_file, destination_file):
    with open(source_file, 'r') as src:
            content = src.read()
    with open(destination_file, 'w') as dest:
            dest.write(content)
    print(f"File copied from '{source_file}' to '{destination_file}'.")
    
path1 = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06/dir-and-files/7)source.txt'
path2 = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06/dir-and-files/7)destination.txt'

copy_file_manual(path1, path2)
