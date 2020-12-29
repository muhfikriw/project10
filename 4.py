f = open("c:/Users/Fikri/Documents/project2.txt", "r")
data = []
data2 = []
data3 = []
for line in f:
    spl = line.split("|")
    data.append(spl[0])
    data2.append(spl[1])
    data3.append(spl[2].strip())

pil = str(input("Masukkan NIM yang mau dicari : "))
if pil in data:
    a = data.index(pil)
    print("\nData Mahasiswa:\nNIM	: ",data[a],"\nNama	: ",data2[a],"\nAlamat	: ",data3[a])
else:
    print("data tidak ditemukan")
