import os
from PIL import Image

ornek_dosya = 'vangogh'
yeniresimler = 'vangogh2'

if not os.path.exists(yeniresimler):
    os.makedirs(yeniresimler)

for dosya in os.listdir(ornek_dosya):
    if dosya.endswith('.jpg') or dosya.endswith('.jpeg'):
        dosya_yolu = os.path.join(ornek_dosya, dosya)
        try:
            with Image.open(dosya_yolu) as resim:
                resim = resim.resize((420, 420), Image.LANCZOS)

                yeniresim_yolu = os.path.join(yeniresimler, dosya)
                resim.save(yeniresim_yolu)
                print(f'Dönüştürüldü: {dosya} -> {yeniresim_yolu}')
        except Exception as e:
            print(f'Hata: {dosya} - {e}')
            #https://pillow.readthedocs.io/en/stable/reference/Image.html
