usia = int(input("Masukkan Umur = "))

if usia >= 0 and usia <= 5:
    print("Balita")
elif usia >= 6 and usia <= 13:
    print("Anak-anak")
elif usia >=13 and usia <= 17:
    print("Remaja")
elif usia >= 18 and usia <= 59:
    print("Dewasa")
elif usia >= 60:
    print("Lansia")
else:
    print("Inputan Salah")