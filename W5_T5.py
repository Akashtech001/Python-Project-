def main():
    print("Program starting.")
    word = ''
    delimiter = ''

    while True:
        print("\nOptions:")
        print("1 - Insert word")
        print("2 - Insert delimiter")
        print("3 - Separate")
        print("0 - Exit program")

        option = input("Your choice: ")

        if option == '1':
            word = input("Insert word: ")
        elif option == '2':
            delimiter = input("Insert delimiter: ")
        elif option == '3':
            if word and delimiter:
                print(delimiter.join(word))
            else:
                print("Please insert both word and delimiter first.")
        elif option == '0':
            print("\nProgram ending.")
            break
        else:
            print("Unknown option! Try again.")

    return None

if __name__ == "__main__":
    main()
