#EMRAN MAHAMUD AKASH
import hashlib

# Constants
FILENAME = "credentials.txt"
SEPARATOR = ";"

def read_credentials():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            return [line.strip().split(SEPARATOR) for line in lines]
    except FileNotFoundError:
        return []

def write_credentials(credentials):
    with open(FILENAME, "w") as file:
        for username, password_hash in credentials:
            file.write(f"{username}{SEPARATOR}{password_hash}\n")

def md5_hexdigest(text):
    return hashlib.md5(text.encode()).hexdigest()

def register_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    password_hash = md5_hexdigest(password)

    credentials = read_credentials()
    credentials.append((username, password_hash))
    write_credentials(credentials)

    print("User registration completed!\n")

def login_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    password_hash = md5_hexdigest(password)

    credentials = read_credentials()
    for stored_username, stored_password_hash in credentials:
        if username == stored_username and password_hash == stored_password_hash:
            print("Authentication successful!\n")
            return True

    print("Authentication failed!\n")
    return False

def main():
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "0":
            print("\nProgram ending.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

