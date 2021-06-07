print("Porsi Terbanyak")
porsi = []

while True:
    n = input("Masukkan jumlah Porsi ('stop' untuk berhenti): ")
    if n == "stop":
        break
    else:
        porsi.append(int(n))
print("penjualan terbanyak dari satu pelanggan hari ini adalah",max(porsi))
