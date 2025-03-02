import os

def list_contents(path):
    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    
    return directories, files, all_items

path = "C:/Users/Admin/OneDrive/Desktop/"
directories, files, all_items = list_contents(path)

print()
print("Directories:", directories)
print("Files:", files)
print("All contents:", all_items)
print()