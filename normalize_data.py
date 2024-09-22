import os
import cv2
import numpy as np

# Folder paths
dataset_folder = 'C:/Users/edana/Desktop/dataset_new/Bird'
images_folder = os.path.join(dataset_folder, 'images')
labels_folder = os.path.join(dataset_folder, 'labels')

# Output folders
normalized_images_folder = os.path.join(dataset_folder, 'normalized_images')
normalized_labels_folder = os.path.join(dataset_folder, 'normalized_labels')
os.makedirs(normalized_images_folder, exist_ok=True)
os.makedirs(normalized_labels_folder, exist_ok=True)

def normalize_image(image):
    """Normalizes the image to the range [0, 1]."""
    normalized_image = image.astype('float32') / 255.0
    return normalized_image

def update_label_coordinates(label_path, original_shape, new_shape):
    """Updates the coordinates in the label file based on the new dimensions."""
    with open(label_path, 'r') as file:
        lines = file.readlines()
    
    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        class_id = parts[0]
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])
        
        # Update coordinates according to the new dimensions
        new_x_center = x_center * new_shape[1] / original_shape[1]
        new_y_center = y_center * new_shape[0] / original_shape[0]
        new_width = width * new_shape[1] / original_shape[1]
        new_height = height * new_shape[0] / original_shape[0]
        
        updated_lines.append(f"{class_id} {new_x_center} {new_y_center} {new_width} {new_height}\n")
    
    return updated_lines

# Normalize images and update labels
for file_name in os.listdir(images_folder):
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        image_path = os.path.join(images_folder, file_name)
        label_path = os.path.join(labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
        
        # Load and normalize the image
        image = cv2.imread(image_path)
        original_shape = image.shape[:2]  # (height, width)
        normalized_image = normalize_image(image)
        
        # Save the normalized image
        normalized_image_path = os.path.join(normalized_images_folder, file_name)
        cv2.imwrite(normalized_image_path, normalized_image * 255.0)  # Convert normalized image back to [0, 255]
        
        # Update the label file and save to the new folder
        if os.path.exists(label_path):
            updated_labels = update_label_coordinates(label_path, original_shape, original_shape)
            normalized_label_path = os.path.join(normalized_labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
            with open(normalized_label_path, 'w') as label_file:
                label_file.writelines(updated_labels)

print("Normalization and label update process completed.")