umur = int(input("Masukkan umur anda: "))

if umur >= 17 and umur <20:
    print("Anda bisa mendapatkan SIM A,SIM C")
elif umur >= 20 and umur <23:
    print("Anda bisa mendapatkan SIM A,SIM C,SIM A UMUM")
elif umur >= 23:
    print("Anda bisa mendapatkan SIM A,SIM C,SIM A UMUM,SIM B")
else:
    print("Anda belum bisa membuat SIM")