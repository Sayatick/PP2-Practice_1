import os

def check_path_access(path):
    print(f"Checking access for: {path}")
    
    # Test if the path exists
    print("Exists:", os.path.exists(path))
    
    # Test if the path is readable
    print("Readable:", os.access(path, os.R_OK))
    
    # Test if the path is writable
    print("Writable:", os.access(path, os.W_OK))
    
    # Test if the path is executable
    print("Executable:", os.access(path, os.X_OK))

# Example usage
path = 'C:/Users/Admin/OneDrive/Desktop/'
check_path_access(path)
