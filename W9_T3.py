# number_analyzer.py; EMRAN MAHAMUD AKASH

def read_file(file_name):
    numbers = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    numbers.append(float(line))
        return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except ValueError:
        print("Error: Invalid data in the file.")
        return None

def calculate_sum(numbers):
    return round(sum(numbers), 1)

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return round(sum(numbers) / len(numbers), 1)

def main():
    numbers = []
    print("Program starting.", end='')  # Avoid newline

    while True:
        print("\nOptions:")
        print("1 - Read file")
        print("2 - Amount of numbers")
        print("3 - Calculate sum")
        print("4 - Calculate average")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == '1':
            file_name = input("Insert file to read: ")
            numbers = read_file(file_name)

        elif choice == '2':
            print(f"Amount of numbers in file: {len(numbers)}")

        elif choice == '3':
            if numbers:
                sum_result = calculate_sum(numbers)
                print(f"Sum of numbers: {sum_result}")
            else:
                print("Error: No numbers loaded. Use option 1 to read a file.")

        elif choice == '4':
            if numbers:
                average_result = calculate_average(numbers)
                print(f"Average: {average_result}")
            else:
                print("Error: No numbers loaded. Use option 1 to read a file.")

        elif choice == '0':
            print("\nProgram ending.")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()


