#karena saya menyimpan file di dokument... jadinya lokasi filenya juga begitu
#jika ingin mengecek ganti saja lokasi filenya sesuai yang ada di lokasi penyimpanan anda

#hanya untuk sandi huruf bukan angka

print("----------------------+ Program Caesar +----------------------\n")
huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
file = input("Masukkan nama file (eg = d:/anyfiles.txt) =  ")
f = open(file,"r")
data = (f.read())
n = int(input("Banyak n yang anda masukkan di project 6 = "))

data = data.upper()  #mengubah huruf besar semua
result = ''

for char in data:
    if char in huruf:
        x = huruf.index(char)
        rumus = (x - n) % 26    #rumus
        conv = huruf[rumus]
        result = result + conv
    else:
        result = result + ' '

data = open("c:/Users/Fikri/Documents/sandiasli.txt", "r")
isi = data.readline()      #untuk mengambil isi file yang akan dicek sudah ada tidaknya biar tidak doble
data.close()               #karena kode cuma 1 baris jadi saya bikin cuma 1 baris saja tidak doble kode

f = open("c:/Users/Fikri/Documents/sandiasli.txt", "a+")
if result != isi:     #pengecekkan dobel tidaknya isi file
    f.write(result)
f.close

f = open("c:/Users/Fikri/Documents/sandiasli.txt", "r")
baca = f.readline()
print("\n----------------------+ OUTPUT +----------------------")
print("hasil pengembalian kode anda = ", baca)