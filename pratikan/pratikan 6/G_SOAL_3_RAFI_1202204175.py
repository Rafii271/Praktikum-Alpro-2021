nama = input("Nama :")
nim = input("Nim :")
kelas = input("Kelas :")
asal = input("Daerah asal :")

file_data = open("galang.txt", "x")
file_data = open("galang.txt", "w")

file_data.write(f"Nama\t\t: {nama}\nNIM\t\t\t: {nim}\nKelas\t\t: {kelas}\nDaerah Asal\t: {asal}")

file_data.close()

