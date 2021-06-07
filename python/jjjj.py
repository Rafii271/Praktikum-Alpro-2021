nama = input("Nama :")
nim = input("Nim :")
kelas = input("Kelas :")
asal = input("Daerah asal :")
file_data = open("galang.txt","w")
file_data = open("galang.txt","r+")

file_data.write(f"Nama\t\t: {nama}\nNIM\t\t: {nim}\nKelas\t\t: {kelas}\nDaerah Asal\t: {asal}")

file_data.close()
