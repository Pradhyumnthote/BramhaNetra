import os

barakhadi = [
    
    'ष','षा',' षि',' षी',' षु ','षू ','षे ','षै ','षो ','षं']


# Specify the parent directory where you want to create the folders
parent_directory = "page3"

# Create folders
for folder_name in barakhadi:
    folder_path = os.path.join(parent_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_name}' created at '{folder_path}'")
