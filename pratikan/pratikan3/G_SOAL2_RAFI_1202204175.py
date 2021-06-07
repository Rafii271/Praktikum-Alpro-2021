print("<<< PROGRAM KELIPATAN ANGKA >>>")

batas = int(input("Masukkan batas angka: "))
kelipatan = int(input("Masukkan kelipatan angka: "))

for x in range(0,batas,kelipatan):
    print(x,end=" ")