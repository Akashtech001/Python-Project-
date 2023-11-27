def main():
    print("Program starting.")
    print("This program can analyse list of names.")
    try:
        file_name = input("Insert filename: ")
        with open(file_name, 'r') as file:
            names = file.read().splitlines()

        # Filter out any empty names
        names = [name for name in names if name]

        if not names:
            print("No valid names found in the file.")
            return
        print(f"Reading and analysing file '{file_name}'.")
        print("Analysis complete.")

        # Calculate the requested aspects
        amount_of_names = len(names)
        shortest_name = min(len(name) for name in names)
        longest_name = max(len(name) for name in names)
        total_length = sum(len(name) for name in names)
        average_name_length = total_length / amount_of_names

        # Print the report
        print("#### REPORT BEGIN ####")
        print(f"Amount of names: {amount_of_names}")
        print(f"Shortest name: {shortest_name}")
        print(f"Longest name: {longest_name}")
        print(f"Average name length: {average_name_length}")
        print("#### REPORT END ####")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    print("Program ending.")
    return None


main()
