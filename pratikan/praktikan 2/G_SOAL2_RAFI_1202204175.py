print("===PROGRAM MIX COLOR RGB===")

warna1 = input("Masukkan warna pertama: ")
warna2 = input("Masukkan warna kedua  : ")

if warna1 == "merah" and warna2 == "biru":
    print(f"Campuran {warna1} dan {warna2} menghasilkan warna ungu")
elif warna1 == "merah" and warna2 == "hijau":
    print(f"Campuran {warna1} dan {warna2} menghasilkan warna kuning")
if warna1 == "hijau" and warna2 == "biru":
    print(f"Campuran {warna1} dan {warna2} menghasilkan warna cyan")    
else:
    print("Mix hanya bisa untuk warna merah/hijau/biru.")