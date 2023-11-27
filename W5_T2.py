USER = "John"
PASS = "MyPass"

def login():
    print("#### Login ####")
    username = input("Insert username: ")
    password = input("Insert password: ")
    if username == USER and password == PASS:
        print(f"Welcome {username}!")
    else:
        print("Wrong credentials.")
    return

def register():
    print("#### Register ####")
    username = input("Insert username: ")
    if username == USER:
        print("User exists!")
    else:
        password = input("Insert password: ")
        print("Registered successfully!")
    return

def main():
    print("Program starting.")
    while True:
        print("Options:\n1 - Login\n2 - Register")
        option = int(input("Your choice: "))
        if option == 1:
            login()
            break
        elif option == 2:
            register()
            break
        else:
            print("Invalid option!")
    print("Program ending.")
    return

if __name__ == "__main__":
    main()

