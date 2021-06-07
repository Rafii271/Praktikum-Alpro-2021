try:
    angka = int(input("Masukan sebuah angka :"))
except ValueError:
    print("Maaf, inputan hanya menerima angka")
else:
    print(angka)