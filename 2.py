while True:
    try:
        text = open("c:/Users/Fikri/Documents/project2.txt", "a+")
        nim = input("Masukkan NIM		: ")
        name = input("Masukkan Nama Mhs	: ")
        alam = input("Masukkan Alamat	 \t: ")
        repeat = input("lagi(y/n)? :")
        if repeat == "n":
            a = nim + "|"
            b = name + "|"
            text.write(a)
            text.write(b)
            text.write(alam + "\n")
            text.close
            text = open("c:/Users/Fikri/Documents/project2.txt", "r")
            print("\nisi file :")
            buka = text.read()
            print(buka)
            break
        elif repeat == "y" :
            a = nim + "|"
            b = name + "|"
            text.write(a)
            text.write(b)
            text.write(alam + "\n")
            text.close
            continue
        else:
            print("inputmu salah")
            exit()
    except ValueError:
        print("input salah")