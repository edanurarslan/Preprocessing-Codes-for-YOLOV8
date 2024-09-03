import os

# Dosyaların bulunduğu klasörün yolu
folder_path = 'C:/Users/edana/Desktop/dataset_new/Bird_and_UAV/augmented_images'

# Dosya isimlerini değiştirmek için başlangıç numarası
start_number = 1
end_number = 20

# Klasördeki tüm dosyaları al
files = os.listdir(folder_path)

# Sadece dosya olanları al (klasörleri hariç tut)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Dosyaları sıralı olarak yeniden isimlendirme işlemi
for i, file_name in enumerate(files):
    if i < end_number:
        # Dosyanın uzantısını al
        file_extension = os.path.splitext(file_name)[1]
        # Yeni dosya adını oluştur
        new_name = f"{start_number + i}{file_extension}"
        # Eski ve yeni dosya yollarını oluştur
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        # Dosya ismini değiştir
        os.rename(old_file_path, new_file_path)
        print(f"'{file_name}' dosyası '{new_name}' olarak değiştirildi.")
    else:
        break

print("Dosya isimlendirme işlemi tamamlandı.")