class Kubus:

    def kubus(sisi1):
        v = sisi1 * sisi1 * sisi1
        l = 6 * sisi1 * sisi1
        k = 12 * sisi1
        print("================================")
        print("Kubus 1")
        print(f"Volume\t\t\t: {v} cm^3 ")
        print(f"Luas Permukaan\t\t: {l} cm^2")
        print(f"Keliling\t\t: {k} cm")

    sisi1 = int(input("Masukkan sisi Kubus 1 : "))
    sisi2 = int(input("Masukkan sisi Kubus 2 : "))

    kubus(sisi1)
    kubus(sisi2)