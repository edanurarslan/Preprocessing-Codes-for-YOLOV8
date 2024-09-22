import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import imgaug.augmenters as iaa
import shutil

# Folder paths
dataset_folder = 'C:/Users/edana/Desktop/dataset_new/Bird'
images_folder = os.path.join(dataset_folder, 'images')
labels_folder = os.path.join(dataset_folder, 'labels')
augmented_images_folder = os.path.join(dataset_folder, 'augmented_images')
augmented_labels_folder = os.path.join(dataset_folder, 'augmented_labels')

# Create output folders
os.makedirs(augmented_images_folder, exist_ok=True)
os.makedirs(augmented_labels_folder, exist_ok=True)

# Define an augmentation chain using imgaug for data augmentation processes
augmenter = iaa.Sequential([
    iaa.Fliplr(0.5),  # Horizontal flip
    iaa.Flipud(0.5),  # Vertical flip
    iaa.Affine(rotate=(-25, 25)),  # Random rotation
    iaa.Affine(scale=(0.8, 1.2)),  # Random scaling
    iaa.AdditiveGaussianNoise(scale=(0, 0.05*255)),  # Add random noise
    iaa.Multiply((0.8, 1.2)),  # Color adjustment (randomly increase/decrease brightness)
    iaa.LinearContrast((0.75, 1.5)),  # Contrast adjustment
    iaa.CropAndPad(percent=(0, 0.1)),  # Random cropping and padding
    iaa.GaussianBlur(sigma=(0, 3.0))  # Blurring
])

def color_jitter(image):
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(np.random.uniform(0.8, 1.2))  # Random color adjustment
    return image

# Process label files and images
for file_name in os.listdir(images_folder):
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        image_path = os.path.join(images_folder, file_name)
        label_path = os.path.join(labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
        
        # Open the image
        image = Image.open(image_path)
        image_np = np.array(image)

        # Augment with imgaug
        image_aug_np = augmenter.augment_image(image_np)
        image_aug = Image.fromarray(image_aug_np)

        # Color adjustment
        image_aug = color_jitter(image_aug)

        # Save the augmented image
        augmented_image_path = os.path.join(augmented_images_folder, file_name)
        image_aug.save(augmented_image_path)

        # Copy the label file (In this example, no changes are made to the labels)
        if os.path.exists(label_path):
            shutil.copy(label_path, augmented_labels_folder)

print("Data augmentation completed.")