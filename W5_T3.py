def frame(input_text):
    length = len(input_text)
    border = '*' * (length + 4)
    framed_text = f'* {input_text} *'

    print(border)
    print(framed_text)
    print(border)
    
    return None

def main():
    print("Program starting.")
    user_input = input("Insert sentence: ")
    
    if user_input.strip():  # Check if the input is not empty or only contains whitespace
        print()
        frame(user_input)
    else:
        print("No input provided.")
    
    print("\nProgram ending.")
    
    return None

if __name__ == "__main__":
    main()

