class App:

    def login(self):
        user = input("Username \t: ")
        pw = input("Password \t: ")

        if user == "alpro" and pw == "daspro":
            print('''
            Login Success
            Welcome to my app!!
            ''')
    def logout(self):
        print("You're successfully log out. Thank you for using me ")

if __name__ == "__main__":
    state = False
    while True:
        print("""
        1. Login
        2. Logout
        """)
    u_input = int(input("Choose Menu? \t: "))

    if u_input == 1:
        app = App()
        app.login()
        state = True
        print()
    elif u_input == 2 and state == False:
        print('''\n!!! Login First!!\n ''')
    elif u_input == 2 and state == True:
        app.logout()
        c
    else:
        print(''' !!No Option!! ''')