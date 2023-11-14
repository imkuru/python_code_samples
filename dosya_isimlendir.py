import os

klasor = '/Users/ibrahimkuru/Desktop/adsız klasör/arkaplan/'

dosyalar = os.listdir(klasor)

yeni_ad = 'a'
indeks = 23

emin = 'e' #input('Emin misiniz? (e)')

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