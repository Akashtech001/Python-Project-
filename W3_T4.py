# Program starting
print("Program starting.")
# This is a menu driven program, where you can choose which operation the program performs
print("This is a menu driven program, where you can choose which operation the program performs.")
# Prompt username first
name = input("Before the menu, please insert your name: ")
# Make program menu with following options
print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
# Prompt user to choose between the options
choice = int(input("Your choice: "))
# Perform actions based on the user input
if choice == 1: # If user chooses option 1
    # Print welcome message
    print(f"Welcome {name}!")
elif choice == 2: # If user chooses option 2
    # Print the name backwards
    backwards = name[::-1] # Reverse the name using slicing
    print(f'Your name backwards is "{backwards}".')
elif choice == 3: # If user chooses option 3
    # Print the first character
    first = name[0] # Get the first character using indexing
    print(f'The first character in name "{name}" is "{first}".')
elif choice == 4: # If user chooses option 4
    # Show the amount of characters in the name
    length = len(name) # Get the length of the name using len function
    print(f'There are {length} characters in the name "John"')
elif choice == 0: # If user chooses option 0
    # Exit
    print("Exiting...") # Exit the program
else: # If user chooses an unknown option
    # Print an error message
    print("Unknown option.")

# Program ending
print("Program ending.")
