def printext():
    text = open("c:/Users/Fikri/Documents/pro1.txt", "r")
    text = text.read()
    return text
def bikinlist():
    file = open("c:/Users/Fikri/Documents/pro1.txt", "r")
    lis = []
    for angka in file:
        lis.append(int(angka))
    return lis

#output text
a = printext()
print(a)

#rumus
lisang = bikinlist()
x = 0
gen = 0
gan = 0
for ang in lisang:
    cek = lisang[x]
    if ang % 2 == 0:
        gen += 1
    if ang % 2 == 1:
        gan += 1
    x += 1


#output akhir :)
print("\n\nOutputnya:\nBanyaknya bilangan genap: ", gen, "\nBanyaknya bilangan ganjil: ",gan)