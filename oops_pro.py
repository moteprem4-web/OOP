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
            pass

        elif user_input=="2":
            pass

        elif user_input=="3":
            pass

        elif user_input=="4":
            pass

        else:
            exit()




c1=Chatbook()
c1.menu()