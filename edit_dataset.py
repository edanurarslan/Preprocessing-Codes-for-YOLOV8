import os
import shutil

# Path to the folder containing the images
image_folder = 'C:/Users/edana/Desktop/newly_dataset/UAV/images/kaldırılacaklar'

# Path to the folder containing the txt files
txt_folder = 'C:/Users/edana/Desktop/newly_dataset/UAV/labels'

# Target folder where txt files will be moved
target_folder = 'C:/Users/edana/Desktop/newly_dataset/UAV/labels/kaldırılacaklar labels'

# Create the target folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Get the names of image files (without extensions)
image_files = set(os.path.splitext(f)[0] for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)))

# Check the txt files in the txt folder
for txt_file in os.listdir(txt_folder):
    file_name, extension = os.path.splitext(txt_file)
    
    # If the txt file name matches the image files, move it
    if extension == '.txt' and file_name in image_files:
        old_path = os.path.join(txt_folder, txt_file)
        new_path = os.path.join(target_folder, txt_file)
        
        # Move the txt file to the new folder
        shutil.move(old_path, new_path)
        print(f"{txt_file} has been moved to the kaldır_label folder.")

print("Process completed.")

#2

# Path to the folder containing the images
image_folder = 'C:/Users/edana/Desktop/newly_dataset/UAV/images'

# Path to the folder containing the TXT files
txt_folder = 'C:/Users/edana/Desktop/newly_dataset/UAV/labels'

# Check for extensions other than JPEG and JPG and delete them
for file in os.listdir(image_folder):
    file_path = os.path.join(image_folder, file)
    
    # If the file is an image file
    if os.path.isfile(file_path):
        file_name, extension = os.path.splitext(file)
        extension = extension.lower()  # Convert the extension to lowercase
        
        # If the extension is not JPEG or JPG, delete the file
        if extension not in ['.jpeg', '.jpg']:
            os.remove(file_path)
            print(f"{file} has been deleted from the image folder.")
            
            # Check for the same named txt file in the txt folder and delete it
            txt_file = f"{file_name}.txt"
            txt_file_path = os.path.join(txt_folder, txt_file)
            
            if os.path.exists(txt_file_path):
                os.remove(txt_file_path)
                print(f"{txt_file} has been deleted from the txt folder.")

print("Process completed.")

#3

# Path to the folder containing the images
image_folder = 'C:/Users/edana/Desktop/newly_dataset/Bird/images'

# Path to the folder containing the TXT files
txt_folder = 'C:/Users/edana/Desktop/newly_dataset/Bird/labels'

# Check for extensions other than JPEG and JPG and delete them
for file in os.listdir(image_folder):
    file_path = os.path.join(image_folder, file)
    
    # If the file is an image file
    if os.path.isfile(file_path):
        file_name, extension = os.path.splitext(file)
        extension = extension.lower()  # Convert the extension to lowercase
        
        # If the extension is not JPEG or JPG, delete the file
        if extension not in ['.jpeg', '.jpg']:
            os.remove(file_path)
            print(f"{file} has been deleted from the image folder.")
            
            # Check for the same named txt file in the txt folder and delete it
            txt_file = f"{file_name}.txt"
            txt_file_path = os.path.join(txt_folder, txt_file)
            
            if os.path.exists(txt_file_path):
                os.remove(txt_file_path)
                print(f"{txt_file} has been deleted from the txt folder.")

print("Process completed.")