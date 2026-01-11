users = {}

def signup():
    username = input("Create Username: ")

    if username in users:
        print("User already exists")
        return

    password = input("Create Password: ")

    if len(password) < 4:
        print("Password must be at least 4 characters")
        return

    users[username] = password
    print("Signup Successful")

def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in users and users[username] == password:
            print("Login Successful")
            return
        else:
            attempts -= 1
            print("Wrong credentials. Attempts left:", attempts)

    print("Account Locked")

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank You")
        break
    else:
        print("Invalid choice")
