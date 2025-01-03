# Identifying-the-artist-from-a-work-of-art

Projemizin amacı resimlerin hangi sanatçıya ait olduğunu bulan bir yapay zeka yapmak.
Bunun için 10 tane sanatçı seçtik.
selenium_veritopla, veriCekme kodları resimleri internet ortamından çekmek için kullandığımız kodlardır.
Her ikisinde de crawler olarak selenium kullanılmıştır.
cozunurluk kodu resimlerin hepsini ortak bir çözünürlükte toplamaktadır.
veriArttırma kodu veri arttırma metotlarını kullanan ve bir resimden farklı istediğimiz kadar resim oluşturduğumuz kodtur. 
Vs code, pyhton ve kütüphaneleri kullanılarak hazırlanmıştır.
Kullanılan kütüphaneler: Pillow(Image), numpy, imgaug(augmenters),selenium ve hazır python kütüphaneleri(os,requests,time)
Kodların çalışması için gerekli kütüphaneler indirilmeli
veriCekme ve selenium_veritopla kodlarında gidilecek sitenin url'si girilmeli ve indirilecek klasör bilgileri kodun üstünde değiştirilmelidir. 
cozunurluk kısmında klasör bilgileri ve istenilen cozunurluk kodun üstünde değiştirilmelidir.
Görüntülerin bulunduğğu drive linki:
https://drive.google.com/drive/folders/1KMNpIQ-g7FfmpX2NEQwva1Rf39VPX39E

Bu proje, on farklı sanatçının 50.000'den fazla eserinden oluşan geniş bir veri setini analiz ederek, bir sanat eserinin hangi sanatçıya ait olduğunu yüksek doğrulukla belirleyebilecek bir yapay zeka modeli geliştirmeyi amaçlamaktadır. 
Sanat dünyasında, eserlerin doğru şekilde sınıflandırılması ve sanatçılara özgü tarzların analiz edilmesi hem kültürel hem de akademik anlamda büyük bir öneme sahiptir. 

Projede, derin öğrenme tabanlı transformer modelleri kullanılarak modern yapay zeka tekniklerinden faydalanılacaktır Farklı transformer modelleriyle karşılaştırmalı analiz yapılacak ve her bir modelin performansı değerlendirilecektir. 
Veri seti, sanatçılara ait eserlerin görsel özelliklerini doğru şekilde algılayabilmesi için veri artırma ve boyutlandırma teknikleriyle optimize edilmiştir. 

Proje süresince, Google Colab platformunun ücretsiz GPU olanakları kullanılarak ortak bir eğitim süreci yürütülmekte olup, model geliştirme süreci, optimize edilmiş bir eğitim stratejisiyle desteklenmektedir. 
Nihai hedefimiz, hem akademik hem de endüstriyel kullanım için etkili bir yapay zeka sınıflandırma çözümü geliştirmek ve sanat eserlerinin analizine yönelik inovatif bir yaklaşım sunmaktır. 
![matris](https://github.com/user-attachments/assets/1f9c87a3-0e2d-46d7-8ce1-b6ffec14c803)


Görüntü Testi Arayüzü:
![son](https://github.com/user-attachments/assets/166eae72-a03e-4ce9-828d-54e8ed737383)


