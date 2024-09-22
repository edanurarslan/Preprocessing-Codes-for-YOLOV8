import os
import glob

# Specify the folder path where the .txt files are located
folder_path = "C:/Users/edana/Desktop/newly_dataset/UAV/labels"

# Find all .txt files in the folder
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

# Process each .txt file
for file_path in txt_files:
    # Read the content of the file and write to a new list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Change '2's at the beginning of lines to '1's
    new_lines = []
    for line in lines:
        if line.startswith("2"):
            new_lines.append("1" + line[1:])  # Change the first character
        else:
            new_lines.append(line)

    # Write the changes back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

    print(f"Processing of file {file_path} is complete.")

print("Processing of all files is complete.")