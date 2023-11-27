def decorate_file_content(file_name):
    content = ""
    try:
        with open(file_name, 'r') as file:
            content += f"#### START: {file_name} ####\n"
            content += file.read()
            content += f"\n#### END: {file_name} ####"
    except FileNotFoundError:
        content = f"File '{file_name}' not found."

    return content + "\n"

def main():
    print("Program starting.")
    print("This program can read a file.")
    file_name = input("Insert filename: ")
    decorated_content = decorate_file_content(file_name)
    print(decorated_content, end='')
    print("Program ending.")
    return None  # Single return statement, followed by an empty line

if __name__ == "__main__":
    main()
