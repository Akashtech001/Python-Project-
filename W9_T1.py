########################################################
# Task
# - W9_T1
# Developer
# - EMRAN MAHAMUD AKASH
########################################################

import time

def pause_for_1_second():
    print("Paused for 1.0 seconds.")
    time.sleep(1)
    print("Unpaused.")

def custom_pause(seconds):
    print(f"Paused for {seconds} seconds.")
    time.sleep(seconds)
    print("Unpaused.")

def display_menu():
    print("\nOptions:")
    print("1 - Pause for 1 second")
    print("2 - Pause")
    print("0 - Exit")

def main():
    print("Program starting.", end='')

    while True:
        display_menu()

        choice = input("Your choice: ")

        if choice == '1':
            pause_for_1_second()
        elif choice == '2':
            seconds = float(input("Insert seconds: "))
            custom_pause(seconds)
        elif choice == '0':
            print("\nProgram ending.")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

