import json
import os

#Mask R CNN için hazırlanan json dosyası içinden veri seçmek için kullanılır.

#örnek: json dosyasının içinde 1000 kayıt olduğunu varsayalım. 
#Kullanılmak istenen resim dosyaları bir klasöre toplanır.
#Bu kod ile klasördeki resim dosyalarına ait json verileri alınarak yeni bir json dosyası oluşturulur.

jsondosyaadi = "aaa.json" # tüm işaretli verilerin olduğu json dosyası
yeni_json_dosyasi = "bbb.json" # yeni oluşturulacak json dosyası
klasor = r'E:\python\coronary\ydrm75xywg-1\ydrm75xywg-1\test2\test\Yeni klasör' # resimlerin olduğu klasor

with open(jsondosyaadi) as dosya:
  file_contents = dosya.read()

json_data = json.loads(file_contents)

dosyalar = os.listdir(klasor)
yeni_dosya = open(yeni_json_dosyasi, 'w')
yeni_dosya.write("{")

virgul = ''

for sira in json_data:
    sec = json_data[sira]
    if sec['filename'] in dosyalar:
        dt = json_data[sira]
        str_json = json.dumps(dt)
        yeni_dosya.write(virgul + '"' + sira + '":')
        yeni_dosya.write(str_json)
        virgul = ', '
    
yeni_dosya.write("}")
yeni_dosya.close()
print("Bitti.")
