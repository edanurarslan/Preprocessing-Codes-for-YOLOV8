import os

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird_and_UAV/augmented_images'

# Starting number for renaming the files
start_number = 1
end_number = 20

# Get all files in the folder
files = os.listdir(folder_path)

# Only get the files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Sequentially rename the files
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create the old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")