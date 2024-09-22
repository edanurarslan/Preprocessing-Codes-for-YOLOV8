import os
import cv2

# Folder paths
dataset_folder = 'C:/Users/edana/Desktop/dataset_new/Bird'
images_folder = os.path.join(dataset_folder, 'images')
labels_folder = os.path.join(dataset_folder, 'labels')
resized_images_folder = os.path.join(dataset_folder, 'resized_images')
resized_labels_folder = os.path.join(dataset_folder, 'resized_labels')

# Target dimensions for resizing
new_width = 256
new_height = 256

# Create output folders
os.makedirs(resized_images_folder, exist_ok=True)
os.makedirs(resized_labels_folder, exist_ok=True)

# Process images and labels
for file_name in os.listdir(images_folder):
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        # Read the image file
        image_path = os.path.join(images_folder, file_name)
        image = cv2.imread(image_path)
        h, w = image.shape[:2]

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        resized_image_path = os.path.join(resized_images_folder, file_name)
        cv2.imwrite(resized_image_path, resized_image)

        # Read and update the label file
        label_path = os.path.join(labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
        if os.path.exists(label_path):
            resized_label_path = os.path.join(resized_labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
            with open(label_path, 'r') as f:
                lines = f.readlines()
            with open(resized_label_path, 'w') as f:
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        label, x1, y1, x2, y2 = parts
                        # Adjust coordinates for the resized image
                        x1 = int(float(x1) * new_width / w)
                        y1 = int(float(y1) * new_height / h)
                        x2 = int(float(x2) * new_width / w)
                        y2 = int(float(y2) * new_height / h)
                        f.write(f"{label} {x1} {y1} {x2} {y2}\n")

print("The resizing of images and updating of labels has been completed.")