# Program starting
print("Program starting.")
# Testing decision structures
print("Testing decision structures.")
# Prompt user to insert a number
num = int(input("Insert a number: "))
# Display menu
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In chained if-statements")
print("0 - Exit")
# Prompt user to choose option
choice = int(input("Your choice: "))
# Apply following math operations in the options 1 & 2
if choice == 1: # If user chooses option 1
    print("Using one multi-branched decision structure.")
    # One multi-branched decision structure
    if num >= 400: # If value is 400 or more
        num += 44 # Add 44 to the existing value
    elif num >= 200: # If value is 200 or more
        num += 22 # Add 22 to the existing value
    elif num >= 100: # If value is 100 or more
        num += 11 # Add 11 to the existing value
    # Show the result to the user
    print(f"Result is {num}")
elif choice == 2: # If user chooses option 2
    print("Using chained if-statements.")
    # Chained if-statements structure
    if num >= 400: # If value is 400 or more
        num += 44 # Add 44 to the existing value
    if num >= 200: # If value is 200 or more
        num += 22 # Add 22 to the existing value
    if num >= 100: # If value is 100 or more
        num += 11 # Add 11 to the existing value
    # Show the result to the user
    print(f"Result is {num}")
elif choice == 0: # If user chooses option 0
    print("Exiting...") # Exit the program
else: # If user chooses an unknown option
    print("Unknown option.") # Print an error message

# Program ending
print("Program ending.")
