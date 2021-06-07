class Kalkulator:

    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y
    
    print("Program Kalkulator Sederhana")
    print("""
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Keluar
    """)

    pilihan = input("Pilihan Anda (1/2/3/4): ")

    num1 = int(input("Masukkan bilangan pertama: "))
    num2 = int(input("Masukkan bilangan kedua: "))
    if pilihan == '1':
        print("Hasil Penjumlahannya adalah", add(num1,num2))
    elif pilihan == '2':
        print("hasil Pengurangannya adalah", subtract(num1,num2))
    elif pilihan == '3':
        print("Hasil Perkaliannya adalah", multiply(num1,num2))
    elif pilihan == '4':
        print("Hasil Perkaliannya adalah", divide(num1,num2))
    elif pilihan == '5':
        print("Anda Berhasil Keluar")
    else:
        print("Input salah")