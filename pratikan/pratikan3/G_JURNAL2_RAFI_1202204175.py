print("=== SELAMAT DATANG DI PROGRAM BUTIK")
print("""
1. Kaos
2. Kemeja
3. Jas
4. Selesai
""")

while True:
    a = input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : ")
    if a == 1:
        harga = int(25.000)
        print("Kaos Ditambahkan")
    elif a == 2:
        harga = int(50.000)
        print("Kemeja Ditambahkan")
    elif a == 3:
        harga = int(100.000)
        print("Jas Ditambahkan")
    else:
        break