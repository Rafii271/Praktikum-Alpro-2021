while True:
    jumlah = int(input("Masukkan banyak barang belanjaan: "))
    harga = int(input("Masukkan harga barang: "))
    total = (jumlah * harga)
    if total > 75000:
        disc = (total*0.80)
        print("Total belanjaan sebelum diskon Rp. ",total)
        print("Total belanjaan setelah diskon Rp. ",disc)
        break
    else:
        print("Total belanjaan yang harus dibayar",total)
        break