import os
import shutil

# Klasörlerin yollarını belirleyin
images_folder = 'C:/Users/edana/Desktop/dataset/images'
labels_folder = 'C:/Users/edana/Desktop/dataset/labels'
classes_file = 'C:/Users/edana/Desktop/dataset/classes.txt'

# Çıktı klasörleri
output_folders = {
    'Bird': {'images': 'Bird/images', 'labels': 'Bird/labels'},
    'UAV': {'images': 'UAV/images', 'labels': 'UAV/labels'},
    'Bird and UAV': {'images': 'Bird_and_UAV/images', 'labels': 'Bird_and_UAV/labels'},
}

# Çıktı klasörlerini oluşturun
for output in output_folders.values():
    os.makedirs(output['images'], exist_ok=True)
    os.makedirs(output['labels'], exist_ok=True)

# Sınıfları yükleyin
with open(classes_file, 'r') as file:
    classes = [line.strip() for line in file.readlines()]

# Resim formatları
image_extensions = ['.jpg', '.jpeg', '.webp']

# Etiket dosyalarını işle
for label_file in os.listdir(labels_folder):
    label_path = os.path.join(labels_folder, label_file)
    
    # İlgili görüntü dosyasını bulmak için uzantıları dene
    image_found = False
    for ext in image_extensions:
        image_path = os.path.join(images_folder, label_file.replace('.txt', ext))
        if os.path.exists(image_path):
            image_found = True
            break
    
    if not image_found:
        print(f"Warning: Image file not found for label: {label_file}")
        continue

    with open(label_path, 'r') as file:
        lines = file.readlines()

    labels = set()
    for line in lines:
        class_id = int(line.split()[0])
        labels.add(classes[class_id])

    # Sınıfa göre dosyaları taşı
    if 'Bird' in labels and 'UAV' in labels:
        category = 'Bird and UAV'
    elif 'Bird' in labels:
        category = 'Bird'
    elif 'UAV' in labels:
        category = 'UAV'
    else:
        continue  # İlgili kategori bulunamadıysa geç

    # Dosyaları ilgili klasöre taşı
    shutil.copy(image_path, output_folders[category]['images'])
    shutil.copy(label_path, output_folders[category]['labels'])

print("İşlem tamamlandı.")