import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import imgaug.augmenters as iaa
import shutil

# Klasör yolları
dataset_folder = 'C:/Users/edana/Desktop/dataset_new/Bird'
images_folder = os.path.join(dataset_folder, 'images')
labels_folder = os.path.join(dataset_folder, 'labels')
augmented_images_folder = os.path.join(dataset_folder, 'augmented_images')
augmented_labels_folder = os.path.join(dataset_folder, 'augmented_labels')

# Çıktı klasörlerini oluşturun
os.makedirs(augmented_images_folder, exist_ok=True)
os.makedirs(augmented_labels_folder, exist_ok=True)

# Veri artırma işlemleri için imgaug kullanarak bir artırma zinciri tanımlayın
augmenter = iaa.Sequential([
    iaa.Fliplr(0.5),  # Yatay çevirme
    iaa.Flipud(0.5),  # Dikey çevirme
    iaa.Affine(rotate=(-25, 25)),  # Rastgele döndürme
    iaa.Affine(scale=(0.8, 1.2)),  # Rastgele yakınlaştırma
    iaa.AdditiveGaussianNoise(scale=(0, 0.05*255)),  # Rastgele gürültü ekleme
    iaa.Multiply((0.8, 1.2)),  # Renklendirme (görselin parlaklığını rastgele artırma/azaltma)
    iaa.LinearContrast((0.75, 1.5)),  # Kontrast artırma
    iaa.CropAndPad(percent=(0, 0.1)),  # Görseli rastgele kesme ve padleme
    iaa.GaussianBlur(sigma=(0, 3.0))  # Blurlama
])

def color_jitter(image):
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(np.random.uniform(0.8, 1.2))  # Rastgele renk ayarı
    return image

# Etiket dosyalarını ve görselleri işle
for file_name in os.listdir(images_folder):
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        image_path = os.path.join(images_folder, file_name)
        label_path = os.path.join(labels_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.webp', '.txt'))
        
        # Görseli aç
        image = Image.open(image_path)
        image_np = np.array(image)

        # imgaug ile artırma
        image_aug_np = augmenter.augment_image(image_np)
        image_aug = Image.fromarray(image_aug_np)

        # Renklendirme işlemi
        image_aug = color_jitter(image_aug)

        # Artırılmış görüntüyü kaydet
        augmented_image_path = os.path.join(augmented_images_folder, file_name)
        image_aug.save(augmented_image_path)

        # Etiket dosyasını kopyala (Bu örnekte etiketlerde değişiklik yapılmaz)
        if os.path.exists(label_path):
            shutil.copy(label_path, augmented_labels_folder)

print("Veri artırma tamamlandı.")

