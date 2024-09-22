import os

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird_and_UAV/augmented_images'

# Starting number for renaming files
start_number = 1
end_number = 20

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")
 

#2

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird_and_UAV/normalized_images'

# Starting number for renaming files
start_number = 19
end_number = 40

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")


#3

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird/augmented_images'

# Starting number for renaming files
start_number = 1
end_number = 400

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")

#4

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird/normalized_images'

# Starting number for renaming files
start_number = 348
end_number = 800

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")

#5

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird/resized_images'

# Starting number for renaming files
start_number = 695
end_number = 1100

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")

#6

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/UAV/normalized_images'

# Starting number for renaming files
start_number = 418
end_number = 1100

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")

#6

# Path to the folder containing the files
folder_path = 'C:/Users/edana/Desktop/dataset_new/UAV/resized_images'

# Starting number for renaming files
start_number = 835
end_number = 1600

# Get all files in the folder
files = os.listdir(folder_path)

# Keep only files (exclude directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files sequentially
for i, file_name in enumerate(files):
    if i < end_number:
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]
        # Create the new file name
        new_name = f"{start_number + i}{file_extension}"
        # Create old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file_name}' has been renamed to '{new_name}'.")
    else:
        break

print("File renaming process completed.")