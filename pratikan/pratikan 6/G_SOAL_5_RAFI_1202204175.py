un = "4175"
pw = "alproPalingGG"
for i in range(3):
   try:
       username = input("Masukkan Username : ")
       password = input("Masukkan password : ")
       if len(password) < 8:
           raise NameError
       else:
           if un == username and pw == password:
               print("Anda berhasil login!")
               break
           else:
               print("Username atau password salah!")
   except NameError:
       print("Password minimal 8 bro!")
       continue