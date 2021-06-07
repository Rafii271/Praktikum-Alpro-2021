nama = str(input("Nama :"))
jeniskelamin = str(input("Jenis kelamin :"))
umur = str(input("Umur :"))
minggu1 = int(input("Massukan berat badan minggu ke-1 :"))
minggu2 = int(input("Massukan berat badan minggu ke-2 :"))
minggu3 = int(input("Massukan berat badan minggu ke-3 :"))
rata = (minggu1 + minggu2 + minggu3) / 3

print(" Rata-Rata berat badan",nama,rata)