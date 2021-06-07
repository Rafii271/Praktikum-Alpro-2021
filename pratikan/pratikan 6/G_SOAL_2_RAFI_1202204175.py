print("=====operasi pembagian====")
try:
    x = int(input("Masukan angka pertama :"))
    y = int(input("Masukan angka kedua :"))
    hasil = x/y
except ZeroDivisionError:
    print("Anda tidak dapat membagi bilangan dengan angka 0")
else:
    print(f"hasil pembagian {x} dan {y} adalah {hasil}")