print("Program starting.")
# Prompt the user for two integers
print()
start_value = int(input("Insert starting value: "))
stop_value = int(input("Insert stopping value: "))
print()
print("Starting for-loop:")

# Initialize an empty string to store the numbers
numbers_str = ""

# Loop from start_value to stop_value (inclusive)
for i in range(start_value, stop_value + 1):
    numbers_str += str(i) + " "  # Add the current number to the string with a space separator

# Remove the trailing space from the string
numbers_str = numbers_str.rstrip()

# Print the final string of numbers
print(numbers_str)

print("\nProgram ending.")



