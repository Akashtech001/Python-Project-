  # Program starting
print("Program starting.")
print("Insert two integers.")
# Ask two integers from the user
num1 = int(input("Insert first integer: ")) # Insert first integer
num2 = int(input("Insert second integer: ")) # Insert second integer

# Compare the numbers and then announce the greater number
print("\nComparing inserted integers.")
if num1 > num2: # If first integer is greater than second integer
    print("First integer is greater.") # Announce that first integer is greater
elif num1 < num2: # If first integer is less than second integer
    print("Second integer is greater.") # Announce that second integer is greater
else: # If first integer is equal to second integer
    print("Integers are the same.") # Announce that integers are the same

# Create sum of the two integersn
sum = num1 + num2 # Add the two integers together and store the result in sum
print("\nAdding integers together")
print(f"{num1} + {num2} = {sum}") # Show the result to the user

# Check the parity of the sum
print("\nChecking the parity of the sum...")
if sum % 2 == 0: # If sum is divisible by 2
    print("Sum is even.") # Announce that sum is even
else: # If sum is not divisible by 2
    print("Sum is odd.") # Announce that sum is odd

# Program ending
print("Program ending.")
