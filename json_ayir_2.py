import os
import json
import random

# Mask R CNN için hazır olan json annotation dosyasını 
# belirli yüzdelerde bölmek için kullanılır.


#########PARAMETRE AYARLAMALARI #############################

jsondosyaadi = "/Users/ibrahimkuru/Desktop/coronary şeyleri/coronary/dataset/train.json" # tüm işaretli verilerin olduğu json dosyası
yeni_json_dosyasi = "bbb" # yeni oluşturulacak json dosyası
#train için: bbb_train.json, val için: bbb_val.json gibi dosya oluşturulur.

kayit_sayisi = 2247 # json dosyasının içinden toplam alınacak kayıt sayısını tutar.
#8325 dosyadan hazır olan kaç tanesi alınmak isteniyorsa o yazılır.

train_adet = int(kayit_sayisi * 0.8) # istenilen oran yazılarak farklı oranlarda bölünebilir.
val_adet = kayit_sayisi - train_adet # toplam sayıdan train dışındakiler 

############### PARAMETRE AYARLAMA BİTTİ ###################

with open(jsondosyaadi) as dosya:
  file_contents = dosya.read()

json_data = json.loads(file_contents)

yeni_dosya_train = open(yeni_json_dosyasi + '_train.json', 'w')
yeni_dosya_train.write("{")

yeni_dosya_val = open(yeni_json_dosyasi + '_val.json', 'w')
yeni_dosya_val.write("{")

virgul = ''

kullanilanlar = []

while len(kullanilanlar) < train_adet:
    sira = str(random.randint(1, kayit_sayisi))
    if sira not in kullanilanlar:
        kullanilanlar.append(sira)
        dt = json_data[sira]
        str_json = json.dumps(dt)
        yeni_dosya_train.write(virgul + '"' + sira + '":')
        yeni_dosya_train.write(str_json)
        virgul = ', '

virgul = ''
for sira in json_data:
    if sira not in kullanilanlar:
        dt = json_data[sira]
        str_json = json.dumps(dt)
        yeni_dosya_val.write(virgul + '"' + sira + '":')
        yeni_dosya_val.write(str_json)
        virgul = ', '


yeni_dosya_train.write("}")
yeni_dosya_train.close()

yeni_dosya_val.write("}")
yeni_dosya_val.close()

print("Ayrıştırma Bitti.")
