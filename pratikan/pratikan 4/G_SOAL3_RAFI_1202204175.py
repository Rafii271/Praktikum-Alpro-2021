class Person:
    def __init__(self,gender):
        self.gender = gender

    def behaviors(self):
        if self.gender == "Laki-Laki":
            print("""
            I Love you
            Saya Tidak marah kok
            Saya maafkan kamu
            Kembalilah padaku
            Saya tidak takut
            Ini saya ada rezeki buat kamu
            """)
        elif self.gender == "Perempuan":
            print("""
            I Love you
            Saya tidak marah kok
            Saya maafkan kamu
            Kembalilah padaku
            Haduh saya jadi malu 
            Akumah cukup kamu aja
            """)

p1 = Person("Laki-Laki")
p1.behaviors()
p2 = Person("Perempuan")
p2.behaviors()