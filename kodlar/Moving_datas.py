import os
import shutil

# Klasörlerin yollarını tanımlayın
source_folder = 'C:/Users/edana/Desktop/drone_dataset'  # drone_dataset klasörünün yolu
labels_folder = os.path.join(source_folder, 'labels')  # Etiket dosyalarının toplanacağı klasör
images_folder = os.path.join(source_folder, 'images')  # Görsellerin toplanacağı klasör

# Çıktı klasörlerini oluştur
os.makedirs(labels_folder, exist_ok=True)
os.makedirs(images_folder, exist_ok=True)

# Resim formatları
image_extensions = ['.jpg', '.jpeg', '.webp']

# drone_dataset klasöründeki tüm dosyaları işle
for file_name in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file_name)

    # Eğer dosya bir txt dosyasıysa labels klasörüne kopyala
    if file_name.endswith('.txt'):
        shutil.copy(source_path, labels_folder)

    # Eğer dosya bir resim dosyasıysa images klasörüne kopyala
    elif any(file_name.endswith(ext) for ext in image_extensions):
        shutil.copy(source_path, images_folder)

print("Dosyalar başarıyla taşındı.")