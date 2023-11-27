def collect_values():
    values = []
    print("Program starting.")

    while True:
        user_input = input("Insert positive integer: ")

        if not user_input or not user_input.lstrip('-').isdigit():
            print("Inserting values has been stopped.")
            break

        value = int(user_input)

        if value >= 0:
            values.append(value)
        else:
            print("Inserting values has been stopped.")
            break

    return values


def main():
    collected_values = collect_values()

    print("\nValues in the list:")
    print("Values: \n", end="")
    for index, value in enumerate(collected_values):
        print(f"Index: {index} - Value: {value}")

    # Add a line here
    print("\nSorting values.")
    
    sorted_values = sorted(collected_values)

    # Adjust here as well
    print("Values sorted.\n" if sorted_values else "No values to sort.\n")
    print("Values: ")

    for index, value in enumerate(sorted_values):
        print(f"Index: {index} - Value: {value}")

    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()


