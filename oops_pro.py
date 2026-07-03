class Chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=True
        self.menu()


    def menu(self):
        user_input = input("""
=========================================
        Welcome to ChatBook
=========================================

Please choose an option:

1. Sign Up
2. Log In
3. Write a Post
4. Message a Friend
5. Exit

Enter your choice: 
""")

        if user_input=="1":
            self.signup()

            

        elif user_input=="2":
            self.signin()

        elif user_input=="3":
            pass

        elif user_input=="4":
            pass

        else:
            exit()


    def signup(self):
        email=input("Enter your email: ")
        pwd=input("Setup your password Here:")
        self.username=email
        self.password=pwd
        print("Signup successful! You can now log in.")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first by pressing 1 in the main menu.")
        else:
            uname=input("enter your username")
            pwd=input("enter your password here")

            if self.username==uname and self.password==pwd:
                print("login successful")
                self.loggedin=True

            else:
                print("please input correct credentials")
                print("\n")
                self.menu()
            


c1=Chatbook()
c1.menu()