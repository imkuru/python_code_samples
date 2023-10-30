import os

klasor = "/Users/ibrahimkuru/Documents/androidstudio/learnmate/resimler/renkli/araclar/ikitekerli/"

dosyalar = os.listdir(klasor)

yeni_ad = 'arac'
indeks = 1

emin = input('Emin misiniz? (e)')
if emin == 'e' or emin == 'E':

    for dosya in dosyalar:
        f, e = os.path.splitext(dosya)
        eski = klasor + dosya
        yeni = klasor + yeni_ad + "_" + str(indeks) + e
        os.rename(eski, yeni)
        indeks += 1

    print("bitti")
else:
    print("iptal edildi.")