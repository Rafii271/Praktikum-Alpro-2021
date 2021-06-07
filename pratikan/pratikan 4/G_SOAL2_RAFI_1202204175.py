def Mobil(jenis,merk,harga):
    pajak = harga + (harga * 0.95)
    print("Jenis mobil adalah\t\t:",jenis)
    print("Merk mobil adalah\t\t:",merk)
    print("Total Harga mobil adalah\t:",pajak)
    print()

jumlah = int(input("Ada berapa mobil? "))
print()
for i in range(jumlah):
    jenis = input("Masukkan jenis mobil\t\t:")
    merk = input("Masukkan merk mobil\t\t:")
    harga = int(input("Masukkan harga mobil adalah\t:"))
    print()
    Mobil(jenis,merk,harga)