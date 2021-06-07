print("\t\t NOTES TEMAN BARU ")

n = []

while True:
    nama = input("Masukkan Nama Teman Baru: ")
    if nama == "stop":
        break
    else:
        n.append(nama)
print("\t\t Teman-Teman Baru ")
print(n)