def getIndex():
    data_index = ["galang","dito","iksan baik","indah","nadya"]
    x = int(input("Masukan index :"))
    try:
        print(f"Data index ke -{x} adalah {data_index[x]}")
    except IndexError:
        print("Index tidak ada")

getIndex()