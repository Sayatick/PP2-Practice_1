import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory = os.path.dirname(path)
        print("Directory:", directory)
        
        filename = os.path.basename(path)
        print("Filename:", filename)
    else:
        print(f"The path '{path}' does not exist.")

path = 'C:/Users/Admin/OneDrive/Desktop'
check_path(path)