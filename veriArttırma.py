from imgaug import augmenters as imgment
from PIL import Image
import numpy as np
import os

gorsel_yol = 'E:/sanatçılar/512picasso'
kayit_yol = 'E:/sanatçılar/512picasso5'

augmentation = imgment.Sequential([
        imgment.Affine(
            rotate=(-30,30),
            
            shear=(-15,15)
            ),
        imgment.Multiply((0.5, 1.5)),
        imgment.LinearContrast((0.5, 1.5)),
        imgment.AddToHueAndSaturation((-15,15)),
        imgment.Fliplr(0.5),
        imgment.PerspectiveTransform(scale=(0.01, 0.1)),
        imgment.Crop(percent=(0, 0.2)),
        imgment.AdditiveGaussianNoise(scale=(0, 0.07*255)),


    ])
if not os.path.exists(kayit_yol):
    os.makedirs(kayit_yol)

for j in os.listdir(gorsel_yol):
    
    if j.endswith(".jpg") or j.endswith(".jpeg"):
        gorsel = os.path.join(gorsel_yol, j)
        img = Image.open(gorsel)
        orijinal = os.path.join(f"{kayit_yol}/{j}_original.jpg")
        img.save(orijinal)
        
        img_np = np.array(img)
        for i in range(5):
            arttirilmis_resim = augmentation(images=[img_np])
            arttirilmis_resim = Image.fromarray(arttirilmis_resim[0], 'RGB')
            arttirilmis_resim.save(f"{kayit_yol}/{j}yeniresim{i}.jpg")
            print(f"{j} resim kaydı başarılı!")