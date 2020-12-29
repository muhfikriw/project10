text = open("c:/Users/Fikri/Documents/project2.txt", "r")
line = text.readlines()
text = len(line)
g1 = {}
x = 0
for tex in range(0,text):
        a = line[x]
        spl = a.split("|")
        a = spl[0]
        y = spl[1]
        z = spl[2].replace("\n", "")
        x+=1
        lis = {"nim":a,"name":y,"alamat":z}
        g = {x : lis}
        g1.update(g)
print(g1)