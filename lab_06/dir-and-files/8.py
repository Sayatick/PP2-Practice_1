import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            except Exception as e:
                print(f"Error while deleting '{file_path}': {e}")
        else:
            print(f"Error: No write permission for '{file_path}'.")
    else:
        print(f"Error: The file '{file_path}' does not exist.")

file_path = 'C:/Users/Admin/OneDrive/Desktop/PP2_Practices/lab_06/dir-and-files/8)file2.txt'
delete_file(file_path)
