from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
service = Service(executable_path="edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service = service)

kayit = 'deneme'
url = "https://www.wikiart.org/en/pablo-picasso/all-works#!#filterName:Style_analytical-cubism,resultType:detailed"

driver.get(url)
time.sleep(4)

if not os.path.exists(kayit):
    os.makedirs(kayit)

timeout = 10 
start_time = time.time()

while True:
    try:
        for i in range(10):
            button = driver.find_element(By.TAG_NAME, 'body')
            button.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
        load_more = driver.find_element(By.CLASS_NAME, 'masonry-load-more-button')
        load_more.click()
        time.sleep(3)
        start_time = time.time()
    except:
        if time.time() - start_time > timeout:
            break

gorseller = driver.find_elements(By.TAG_NAME, 'img')
toplam = 0
for gorsel in gorseller:
    time.sleep(0.1)
    try:
        gorsel_adres = gorsel.get_attribute('src')
        if gorsel_adres and gorsel_adres.startswith('http') and 'order@2x.png' not in gorsel_adres:
            gorsel_data = requests.get(gorsel_adres).content 
            gorsel_adi = gorsel_adres.split('/')[-1]
            gorsel_yol = os.path.join(kayit, gorsel_adi)
            with open(gorsel_yol, "wb") as f:
                f.write(gorsel_data)
            toplam+=1
            print(f"{toplam} Success! -> {gorsel_adi}")
    except Exception as e:
        print("Hata -> ", e)
time.sleep(3)
driver.quit()
#Veri çekme işlemlerinin kullanımı dökümantasyonlar ve tech with tim adlı youtube kanalı üzerinden yapılmıştır.
