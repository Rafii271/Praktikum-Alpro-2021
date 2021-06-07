b = str(input("Masukan banyak belanja Dewi: "))
totalbelanja = 0
for i in range(1):
    hargamakanan = int(input("masukan Harga makanan: "))
    hargaminuman = int(input("masukan harga minuman: "))
    totalbelanja += hargamakanan
    totalbelanja += hargaminuman
if(totalbelanja >= 25000):
    print(f'Total yang di bayar dewi adalah RP{totalbelanja*0.2}')
if(totalbelanja < 25000):
    print(f'Total yang di bayar dewi adalah RP{totalbelanja*0.1}')
else:
    print(f'Total yang di bayar dewi adalah RP{totalbelanja}')
