print("\t\t>> Program Matematika <<\n")
set_a = set(range(0,11))
set_b = set(range(6,16))
set_c = set(range(11,21))
print("Set A berisikan angka: ",set_a)
print("Set B berisikan angka: ",set_b)
print("""
Ketik 1 untuk menghitung GABUNGAN antara 2 set
Ketik 2 untuk menghitung IRISAN antara 2 set
Ketik 3 untuk menghitung SELISIH antara 2 set
Ketik 4 untuk membuat SET BARU dan update set A
""")
while True:
    menu = int(input("Pilih menu: "))
    if menu == 1:
        print(set_a.union(set_b))
        print()
    elif menu == 2:
        print(set_a.intersection(set_b))
        print()
    elif menu == 3:
        print(set_a.difference(set_b))
        print()
    elif menu == 4:
        # set_c = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        # set_a = set(range(0,11))
        set_a.update(set_c)
        print("Set A telah diupdate menjadi:", set_a)
        print()
    else:
        print("Kamu hanya boleh pilih menu sampai 4")
        break