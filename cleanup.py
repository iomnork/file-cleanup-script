import os
import shutil

# 👉 Set the directory you want to clean
target_directory = "C:/Users/YourName/Downloads"  # Change this to your folder

# Create a folder to store sorted files (if it doesn't exist)
sorted_folder = os.path.join(target_directory, "Sorted")
os.makedirs(sorted_folder, exist_ok=True)

# Scan through files in the target directory
for filename in os.listdir(target_directory):
    filepath = os.path.join(target_directory, filename)

    # Skip directories
    if os.path.isdir(filepath):
        continue

    # Get the file extension
    _, extension = os.path.splitext(filename)
    extension = extension[1:].lower()  # remove the dot and lowercase it

    if not extension:
        extension = "no_extension"

    # Create a subfolder for this extension
    subfolder_path = os.path.join(sorted_folder, extension)
    os.makedirs(subfolder_path, exist_ok=True)

    # Move the file into the extension-named folder
    destination = os.path.join(subfolder_path, filename)
    shutil.move(filepath, destination)

    print(f"Moved: {filename} → {subfolder_path}")
