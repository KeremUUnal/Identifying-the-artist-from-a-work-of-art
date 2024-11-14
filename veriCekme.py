from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import os
import requests
from PIL import Image
from io import BytesIO
import time

# WebDriver için PATH oluşturur
PATH = "\\edgedriver_win64\\msedgedriver.exe"

# Edge WebDriver'ı başlatmak için Service kullanır
service = Service(PATH)
wd = webdriver.Edge(service=service)


url = 'https://claudemonetgallery.org/the-complete-works.html?ps=96'
wd.get(url)
time.sleep(3)

# İndirilecek klasörü ayarlar
od = 'Eywind'
os.makedirs(od, exist_ok=True)

# Listeleyerek önceki görüntüleri takip eder
downloaded_images = os.listdir(od)  


sayfa_no = 1
downloaded_count = 0

while True:
    # Görselleri indirme işlemi
    images = wd.find_elements(By.TAG_NAME, 'img')
    
    for img in images:
        goruntu_adres = img.get_attribute('src')
        if goruntu_adres and goruntu_adres.startswith('http'):
            # URL parametrelerini kaldır
            img_name = goruntu_adres.split('?')[0].split('/')[-1]

            #Eğer görüntü varsa devam eder 
            if img_name not in downloaded_images:
                try:
                    # Görseli indir ve Pillow ile açar
                    cevap = requests.get(goruntu_adres)
                    image = Image.open(BytesIO(cevap.content))
                    
                    
                    image.save(os.path.join(od, img_name))
                    downloaded_images.append(img_name) 
                    downloaded_count += 1
                    print(f'{img_name} indirildi.')
                except Exception as e:
                    print(f'{img_name} indirilemedi. Hata: {e}')
    
    
    try:
        sonraki_buton = wd.find_element(By.LINK_TEXT, str(sayfa_no + 1))
        sonraki_buton.click()
        sayfa_no += 1
        time.sleep(3)  
    except:
        print("Sonraki sayfa yok, işlem tamamlandı.")
        break

print(f'Toplam indirilen görsel sayısı: {downloaded_count}')

wd.quit()
