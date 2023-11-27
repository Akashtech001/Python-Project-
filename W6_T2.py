def write_info_to_file():
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    age = input("Insert age: ")

    file_name = input("Insert filename: ")

    with open(file_name, 'w') as file:
        file.write(f"{first_name}\n{last_name}\n{age}\n")

    print(f"Writing file '{file_name}'.")
    print("File written.")

def main():
    print("Program starting.")
    print("This program writes files.")
    write_info_to_file()
    print("Program ending.\n")
    return None

if __name__ == "__main__":
    main()
