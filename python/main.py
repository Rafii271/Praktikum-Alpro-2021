'''
{IS :DIberikan Nama Penyakit}
{FS :Obat dari hasil jenis penyakit}

Kamus = penyakit = string

Algoritma:
output("Masukkan Nama Penyakit  : ")
input(penyakit)
if penyakit == "Batuk"
       output(Obatnya adalah : Vicks)
elif penyakit == "Demam"
       output(Obatnya adalah : Paracetamol)
else:
    output(Belum ada obat untuk penyakit tersebut)

'''

penyakit = str(input("Masukkan Nama Penyakit  : "))

if penyakit == "Batuk" :
    print("Obatnya adalah : Vicks")
elif penyakit == "Demam":
    print("Obatnya adalah : Paracetamol")
else:
    print("Belum ada obat untuk penyakit tersebut")