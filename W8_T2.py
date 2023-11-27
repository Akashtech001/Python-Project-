def main():
    print("Program starting.")

    task1_name = input("Give first task name: ")
    task2_name = input("Give second task name: ")

    task1_status = ' '
    task2_status = ' '

    print(f"Task: {task1_name}, status: \"{task1_status}\"")
    print(f"Task: {task2_name}, status: \"{task2_status}\"")

    choice = int(input("\nChange task one (1) or task two (2) status\nYour choice(1 or 2): "))

    if choice == 1:
        task1_status = 'x'
    elif choice == 2:
        task2_status = 'x'

    print(f"Task: {task1_name}, status: \"{task1_status}\"")
    print(f"Task: {task2_name}, status: \"{task2_status}\"")

    print("\nProgram ending.")
    return


if __name__ == "__main__":
    main()
