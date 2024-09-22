import os

# Specify the path to the folder containing images
image_folder = "C:/Users/edana/Desktop/ADİL BİRD/drive-download-20240908T081749Z-001/images"

# Get all files in the folder
for file in os.listdir(image_folder):
    file_path = os.path.join(image_folder, file)

    # If the file is an image file and its extension is not JPEG or JPG, delete it
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()  # Convert file extension to lowercase
        if extension not in ['.jpeg', '.jpg']:
            os.remove(file_path)
            print(f"{file} has been deleted.")

print("Process completed.")

#2


# Specify the paths to the image and txt folders
image_folder = "C:/Users/edana/Desktop/ADİL BİRD/drive-download-20240908T081749Z-001/images"
txt_folder = "C:/Users/edana/Desktop/ADİL BİRD/drive-download-20240908T081749Z-001/labels"

# List the files in the image folder (file names without extensions)
image_files = set(os.path.splitext(f)[0] for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)))

# List the files in the txt folder (file names without extensions)
txt_files = set(os.path.splitext(f)[0] for f in os.listdir(txt_folder) if os.path.isfile(os.path.join(txt_folder, f)))

# Files that are present in both the image and txt folders
common_files = image_files.intersection(txt_files)

# Delete files that are in the image folder but not in the txt folder
for file in os.listdir(image_folder):
    file_name, extension = os.path.splitext(file)
    if file_name not in common_files:
        os.remove(os.path.join(image_folder, file))
        print(f"{file} has been deleted from the image folder.")

# Delete files that are in the txt folder but not in the image folder
for file in os.listdir(txt_folder):
    file_name, extension = os.path.splitext(file)
    if file_name not in common_files:
        os.remove(os.path.join(txt_folder, file))
        print(f"{file} has been deleted from the txt folder.")

print("Process completed.")