alfian = input("Alfian, Masukkan jagoan anda : ")
nopal = input("Nopal, Masukkan jagoan anda : ")

if alfian == "gajah" and nopal == "manusia":
    print("ALFIAN MENANG")
elif alfian == "manusia" and nopal == "gajah":
        print("NOPAL MENANG")
elif alfian == "semut" and nopal == "manusia":
    print("NOPAL MENANG")
elif alfian == "manusia" and nopal == "semut":
        print("ALFIAN MENANG")
elif alfian == "semut" and nopal == "gajah":
    print("ALFIAN MENANG")
elif alfian == "gajah" and nopal == "semut":
        print("NOPAL MENANG")
elif alfian == "gajah" and nopal == "gajah" or alfian == "semut" and nopal == "semut" or alfian == "manusia" and nopal == "manusia":
    print("Pertandingan Seri")
else:
    print("Salah Suit Bambang!")