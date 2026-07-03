class Chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
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
            self.my_post()

        elif user_input=="4":
            self.sendmsg()

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
                self.menu()

            else:
                print("please input correct credentials")
                print("\n")
                self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("write your post here")
            print("your post has been posted successfully")
            print("\n")
            self.menu()
        else:
            print("we need to sigin first to write a post")
            print("\n")
            self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("write your message here")
            frnd=input("whom to send the message")
            print(f"your message has been sent to {frnd} successfully")
        else:
            print("we need to sigin first to send a message")
            print("\n")
            self.menu()



            


c1=Chatbook()
c1.menu()