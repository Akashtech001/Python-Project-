def main():
    print("Program starting.")
    print("This program can copy file.")

    try:
        source_file_name = input("Insert source filename: ")
        with open(source_file_name, 'r') as source_file:
            file_content = source_file.read()

        print(f"Reading file '{source_file_name}' content.")
        print("File content ready in memory.")
        
        target_file_name = input("Insert target filename: ")
        with open(target_file_name, 'w') as target_file:
            target_file.write(file_content)

        print(f"Writing file content into '{target_file_name}'.")
        print("File writing complete.")
    except FileNotFoundError:
        print(f"File '{source_file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    print("Program ending.")
    return None


main()
