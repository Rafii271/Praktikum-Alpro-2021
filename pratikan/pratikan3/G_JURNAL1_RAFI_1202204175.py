for i in range(3):
    a = input("Masukkan username Anda: ")
    b = input("Masukkan password Anda: ")
    if a == "alpro" and b == "daspro123":
        print("Selamat, Anda berhasil login")
        break
    else:
        print("Login gagal, Sisa percobaan login sebanyak",i)
else:
    print("limit login habis")