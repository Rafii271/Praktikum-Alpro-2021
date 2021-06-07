sifat_kamu = set([])
sifat_dia = set([])
while True:
    a = str(input("Masukkan Sifat Kamu : "))
    sifat_kamu.add(a)
    if a == "selesai":
        sifat_kamu.remove("selesai")
        break

while True:
    b = str(input("Masukkan Sifat Dia : "))
    sifat_dia.add(b)
    if b == "selesai":
        sifat_dia.remove("selesai")
        break

print(f"\t\tSIFAT KAMU\n{sifat_kamu}")
print(f"\t\tSIFAT DIA\n{sifat_dia}")
print("\tPersamaan dari sifat kamu dan dia")
print(sifat_dia.intersection(sifat_kamu))