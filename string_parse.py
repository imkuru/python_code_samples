dosya = open('data1.txt', 'r')
yeni = open('data2.txt', 'w')

while True:
    oku = dosya.readline()
    if oku == '':
        break
    oku = oku.replace('\n','')
    yeni.write("['" + oku + "'],\n")

dosya.close()
yeni.close()