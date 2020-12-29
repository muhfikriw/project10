#projet meminta untuk membuat file txt yang sudah berisi bilangan, jadi tidak perlu input


f = open("c:/Users/Fikri/Documents/project5.txt", "r")
print(f.read())
f.close()
f = open("c:/Users/Fikri/Documents/project5.txt", "r")
jml = open("c:/Users/Fikri/Documents/jumlah.txt", "a+")
data = []
data2 = []
x = 0
jml.write("\n")
for line in f:
    spl = line.split("|")
    data.append(spl[0])
    data2.append(spl[1].strip())
    jumlah = int(data[x]) + int(data2[x])
    jml.write(str(jumlah)+"\n")
    x+=1
jml.write("\n")
f.close()
jml.close()

#output
jml = open("c:/Users/Fikri/Documents/jumlah.txt", "r")
baca = jml.read()
print(baca)
jml.close()