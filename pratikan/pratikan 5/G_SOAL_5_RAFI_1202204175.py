print("\t\t === TELYU GAMING === ")
produk = []
harga = []

while True:
    print("""
    1. Daftar Produk
    2. Cek Harga

    0. Exit
    """)

    pilihan = int(input("Masukkan Pilihan kamu: "))
    if pilihan == 1:
        produk.append(input("Masukkan Nama Game: "))
        harga.append(input("Masukkan Harga Game: Rp."))
    elif pilihan == 2:
        cek = input("Masukkan nama game: ")
        if cek == produk:
            print("Harganya Adalah Rp. ",harga)
            break
    elif pilihan == 0:
        break
