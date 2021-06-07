class Student:
    def __init__(self,name,nim,kelas,alamat):
        self.name = name
        self.nim = nim
        self.kelas = kelas
        self.alamat =alamat
    
    def show(self):
        print("Nama\t:" +self.name)
        print("NIM\t:" +self.nim)
        print("Kelas\t:" +self.kelas)
        print("Alamat\t:" +self.alamat)
    
p1 = Student("Ananda","1202190008","SI-43-02","Palangka Raya")
p1.show()
print()
print("Mahasiswa 2")
p2 = Student("Xaximi","12021902937","SI-42-04","Bogor")
p2.show()
print()
print("Mahasiswa 3")
p3 = Student("Rizal","12021287229","SI-43-01","Bandung")
p3.show()
print()
print("mahasiswa 4")
p4 = Student("Rafi","1202204175","SI-44-03","padang")
p4.show()