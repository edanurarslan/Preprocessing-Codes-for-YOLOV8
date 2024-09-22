import os
import shutil

# Define the folder paths
source_folder = 'C:/Users/edana/Desktop/drone_dataset'  # Path to the drone_dataset folder
labels_folder = os.path.join(source_folder, 'labels')  # Folder where label files will be collected
images_folder = os.path.join(source_folder, 'images')  # Folder where images will be collected

# Create output folders
os.makedirs(labels_folder, exist_ok=True)
os.makedirs(images_folder, exist_ok=True)

# Image formats
image_extensions = ['.jpg', '.jpeg', '.webp']

# Process all files in the drone_dataset folder
for file_name in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file_name)

    # If the file is a txt file, copy it to the labels folder
    if file_name.endswith('.txt'):
        shutil.copy(source_path, labels_folder)

    # If the file is an image file, copy it to the images folder
    elif any(file_name.endswith(ext) for ext in image_extensions):
        shutil.copy(source_path, images_folder)

print("Files have been successfully moved.")