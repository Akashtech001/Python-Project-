# calculator_combined.py
# EMRAN MAHAMUD AKASH

def add(first_value, second_value):
    return first_value + second_value

def subtract(minuend, subtrahend):
    return minuend - subtrahend

def multiply(first_value, multiplier):
    return first_value * multiplier

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Can't divide with zero."

def show_options():
    print("\nOptions:")
    print("1 - Add numbers")
    print("2 - Subtract numbers")
    print("3 - Multiply numbers")
    print("4 - Divide numbers")
    print("0 - Exit")

def ask_choice():
    choice = input("Your choice: ")
    return choice

def ask_value(prompt):
    value = float(input(f"Insert {prompt} value: "))
    return value

def main():
    print("Program starting.", end='')

    while True:
        show_options()
        choice = ask_choice()

        if choice == '1':
            value1 = ask_value("first")
            value2 = ask_value("second")
            result = add(value1, value2)
            print(f"{value1} + {value2} = {result}")

        elif choice == '2':
            minuend = ask_value("minuend")
            subtrahend = ask_value("subtrahend")
            result = subtract(minuend, subtrahend)
            print(f"{minuend} - {subtrahend} = {result}")

        elif choice == '3':
            value1 = ask_value("multiplicand")
            value2 = ask_value("multiplier")
            result = multiply(value1, value2)
            print(f"{value1} * {value2} = {result}")

        elif choice == '4':
            dividend = ask_value("dividend")
            divisor = ask_value("divisor")
            result = divide(dividend, divisor)
            # Check if the result is an error before printing
            if isinstance(result, str):
                print(result)
            else:
                print(f"{dividend} / {divisor} = {result}")

        elif choice == '0':
            print("\nProgram ending.")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
