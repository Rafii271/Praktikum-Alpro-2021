def indeks(nilai):
    if nilai >= 80:
        return "A"
    elif 80>nilai>=40:
        return "B"
    else:
        return "C"
try:
    print("Program penentu index")
    nem = float(input("Masukan Nilai Akhir Anda! :"))
    if nem > 100 or nem < 0:
        raise NameError
        print(f"Indeks kamu adalah{indeks(nem)}")
except ValueError:
    print("Input harus berupa float/integer (angka)")
except NameError:
     print("Nilai minimal 0 dan maksimal 100")
finally:
    print("Program selesai")

