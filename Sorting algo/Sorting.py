import os
import shutil
from datetime import datetime

# Define paths
home_directory = r'C:\Users\nmkoninn'
desktop_directory = os.path.join(home_directory, 'Desktop')
downloads_directory = os.path.join(home_directory, 'Downloads')
destination_directory = os.path.join(desktop_directory, 'Organized')

# Create a folder with the current date
current_date = datetime.now().strftime('%Y-%m-%d')
destination_date_folder = os.path.join(destination_directory, current_date)

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_date_folder):
    os.makedirs(destination_date_folder)

# File extensions to ignore
ignored_extensions = ['.sys', '.dll', '.exe']

# Helper function to move file to the respective folder based on its extension
def move_file(file_path, destination_folder):
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()

    # Skip files with ignored extensions
    if extension in ignored_extensions:
        return

    # Create a folder for the file type
    extension_folder = os.path.join(destination_folder, extension[1:].upper() + '_FILES')  # E.g. .txt -> TXT_FILES
    if not os.path.exists(extension_folder):
        os.makedirs(extension_folder)

    # Move the file to the folder
    destination_file_path = os.path.join(extension_folder, file_name)
    if not os.path.exists(destination_file_path):
        shutil.move(file_path, destination_file_path)
    else:
        # If file already exists, add a unique identifier
        base_name, ext = os.path.splitext(file_name)
        counter = 1
        new_file_name = f"{base_name}({counter}){ext}"
        new_file_path = os.path.join(extension_folder, new_file_name)
        while os.path.exists(new_file_path):
            counter += 1
            new_file_name = f"{base_name}({counter}){ext}"
            new_file_path = os.path.join(extension_folder, new_file_name)
        shutil.move(file_path, new_file_path)

# Traverse the specified directories and move files
def organize_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            move_file(file_path, destination_date_folder)

# Organize files from Desktop and Downloads folders
organize_files(desktop_directory)
organize_files(downloads_directory)

print(f"All files from Desktop and Downloads have been organized and moved to: {destination_date_folder}")
