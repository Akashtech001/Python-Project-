print("Program starting.")
print()
# Prompt the user for two integers
start_value = int(input("Insert starting value: "))
stop_value = int(input("Insert stopping value: "))

print()
print("Starting while-loop:")
current_value = start_value  # Initialize current_value to start_value

while current_value <= stop_value:
    if current_value < stop_value:
        print(current_value, end=" ")  # Print the current number with a space separator
    else:
        print(current_value, end="\n")  # Print the current number with a newline to end the line
    current_value += 1  # Increment the current number

print("\nProgram ending.")
