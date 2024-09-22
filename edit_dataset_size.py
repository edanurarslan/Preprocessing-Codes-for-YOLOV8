import os
import random

# Specify the paths to the image and txt folders
image_folder = "C:/Users/edana/Desktop/dene dataset/ZEHRA BIRD/Bird-20240908T072823Z-001/images"
txt_folder = "C:/Users/edana/Desktop/dene dataset/ZEHRA BIRD/Bird-20240908T072823Z-001/labels"

# List the files in the image folder (file names + extensions)
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# List the files in the txt folder (file names + extensions)
txt_files = [f for f in os.listdir(txt_folder) if os.path.isfile(os.path.join(txt_folder, f))]

# Get the names of the image files without extensions
image_files_without_extension = [os.path.splitext(f)[0] for f in image_files]

# Get the names of the txt files without extensions
txt_files_without_extension = [os.path.splitext(f)[0] for f in txt_files]

# Find common file names in both image and txt folders
common_files = list(set(image_files_without_extension).intersection(txt_files_without_extension))

# If there are more than 500 common files, randomly select 500
if len(common_files) > 500:
    common_files = random.sample(common_files, 500)

# Delete files not in the common list from the folders
for f in image_files:
    file_name = os.path.splitext(f)[0]
    if file_name not in common_files:
        image_file_path = os.path.join(image_folder, f)  # Get the full file path
        if os.path.exists(image_file_path):
            os.remove(image_file_path)
            print(f"{image_file_path} has been deleted.")

for f in txt_files:
    file_name = os.path.splitext(f)[0]
    if file_name not in common_files:
        txt_file_path = os.path.join(txt_folder, f)
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
            print(f"{txt_file_path} has been deleted.")

print("Process completed.")

#2

# Specify the paths to the image and txt folders
image_folder = "C:/Users/edana/Desktop/dene dataset/ZEHRA UAV/UAV-20240908T072816Z-001/images"
txt_folder = "C:/Users/edana/Desktop/dene dataset/ZEHRA UAV/UAV-20240908T072816Z-001/labels"

# List the files in the image folder (file names + extensions)
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# List the files in the txt folder (file names + extensions)
txt_files = [f for f in os.listdir(txt_folder) if os.path.isfile(os.path.join(txt_folder, f))]

# Get the names of the image files without extensions
image_files_without_extension = [os.path.splitext(f)[0] for f in image_files]

# Get the names of the txt files without extensions
txt_files_without_extension = [os.path.splitext(f)[0] for f in txt_files]

# Find common file names in both image and txt folders
common_files = list(set(image_files_without_extension).intersection(txt_files_without_extension))

# If there are more than 500 common files, randomly select 500
if len(common_files) > 500:
    common_files = random.sample(common_files, 500)

# Delete files not in the common list from the folders
for f in image_files:
    file_name = os.path.splitext(f)[0]
    if file_name not in common_files:
        image_file_path = os.path.join(image_folder, f)  # Get the full file path
        if os.path.exists(image_file_path):
            os.remove(image_file_path)
            print(f"{image_file_path} has been deleted.")

for f in txt_files:
    file_name = os.path.splitext(f)[0]
    if file_name not in common_files:
        txt_file_path = os.path.join(txt_folder, f)
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
            print(f"{txt_file_path} has been deleted.")

print("Process completed.")

#3

import shutil

# Folders containing image and label files
image_folder = "C:/Users/edana/Desktop/dene dataset/bird/images"
label_folder = "C:/Users/edana/Desktop/dene dataset/bird/labels"

# Main directory where training, validation, and test files will be saved
target_folder = "C:/Users/edana/Desktop/dene dataset/bird"

# Create paths for subfolders for training, validation, and testing
train_dir = os.path.join(target_folder, 'train')
val_dir = os.path.join(target_folder, 'val')
test_dir = os.path.join(target_folder, 'test')

# Create images and labels folders in the subfolders
for dir in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'labels'), exist_ok=True)

# List the image files (with extensions)
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Shuffle the files
random.shuffle(image_files)

# Split 70% for train, 20% for validation, and 10% for test based on the number of files
total_files = len(image_files)
train_count = int(total_files * 0.7)
val_count = int(total_files * 0.2)
test_count = total_files - train_count - val_count  # Remaining files for testing

# Divide the files into sets
train_files = image_files[:train_count]
val_files = image_files[train_count:train_count + val_count]
test_files = image_files[train_count + val_count:]

# Function to move files to the relevant folders
def move_files(file_list, src_img_dir, src_lbl_dir, dst_dir):
    for file_name in file_list:
        base_name, ext = os.path.splitext(file_name)
        img_src = os.path.join(src_img_dir, file_name)
        lbl_src = os.path.join(src_lbl_dir, f"{base_name}.txt")

        img_dst = os.path.join(dst_dir, 'images', file_name)
        lbl_dst = os.path.join(dst_dir, 'labels', f"{base_name}.txt")

        if os.path.exists(img_src) and os.path.exists(lbl_src):
            shutil.copy(img_src, img_dst)
            shutil.copy(lbl_src, lbl_dst)

# Move train, validation, and test sets to the relevant folders
move_files(train_files, image_folder, label_folder, train_dir)
move_files(val_files, image_folder, label_folder, val_dir)
move_files(test_files, image_folder, label_folder, test_dir)

print("Files have been successfully separated into train, val, and test folders!")
