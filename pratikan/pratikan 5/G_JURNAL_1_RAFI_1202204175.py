nama = []
while True:
    print('''
    1.Mendaftarkan Peserta
    2.Menghapus Peserta 
    3.Mengupdate Peserta
    4.Mencetak Semua Peserta

    0.Exit 
    ''')

    pil = int(input("Masukkan Pilihan: "))
    if pil == 1:
        nama.append(input("Masukkan nama peserta: "))
    elif pil == 2:
        nama.remove(input("Masukkan nama peserta: "))
    elif pil == 3:
        temp = input("Masukkan nama peserta yang ingin di update: ")
        index = nama.index(temp)
        nama.remove(temp)
        nama.insert(index,input("Masukkan Nama Peserta Baru: "))
    elif pil == 4:
        print(nama)
    elif pil == 5:
        break
    