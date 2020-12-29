#karena saya menyimpan file di dokument... jadinya lokasi filenya juga begitu
#jika ingin mengecek ganti saja lokasi filenya sesuai yang ada di lokasi penyimpanan anda

#hanya untuk sandi huruf bukan angka

#memebuka file txt
f = open("c:/Users/Fikri/Documents/project7.txt", "r")
print("----------------------+ Program Caesar +----------------------\n")
huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

data = f.read()
n = int(input("banyak n untuk penggeseran kode anda = "))
data = data.upper()   #mengubah huruf besar semua
result = ''

for char in data:
    if char in huruf:
        x = huruf.index(char)
        rumus = (x + n) % 26   #rumus
        conv = huruf[rumus]
        result = result + conv
    else:
        result = result + ' '
f.close()

#output
print("----------------------+ OUTPUT +----------------------\n")
data = open("c:/Users/Fikri/Documents/sandiacak.txt", "r")
isi = data.readline()  #untuk mengambil isi file yang akan dicek sudah ada tidaknya biar tidak doble 
data.close             #karena kode cuma 1 baris jadi saya bikin cuma 1 baris saja tidak doble kode

f = open("c:/Users/Fikri/Documents/sandiacak.txt", "a+")
if result != isi:          #pengecekkan dobel tidaknya isi file
        f.write(result)
f.close


#output
data = open("c:/Users/Fikri/Documents/sandiacak.txt", "r")
baca = data.read()
print("hasil pengacakan kode anda = ", baca)
data.close()
