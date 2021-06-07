x = input("Masukkan bahan : ")

def celana(x):
    if x == "Abaka":
        print("Keluarlah Celana tahan air")    
    elif x == "Batu":
        print("Keluarlah Celana dengan perlindungan maksimal")    
    elif x == "Pandan":
        print("Keluarlah Celana Harum")    
    else:
        print("bahan" + x + "tidak diketahui") 
        
celana(x)