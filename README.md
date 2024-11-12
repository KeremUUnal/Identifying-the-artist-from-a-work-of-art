# Identifying-the-artist-from-a-work-of-art
data collection and augment
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

