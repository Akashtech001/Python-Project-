class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

def set_task_name(task):
    name = input("Set task name: ")
    task.name = name
    print()

def change_task_status(task):
    task.status = 'x' if task.status == ' ' else ' '
    print()

def display_task(task):
    print(f'Task: {task.name}, status: "{task.status}"\n')

def main():
    print("Program starting.")
    task = Task("", " ")

    # Operate
    while True:
        print("Options:")
        print("1 - Set task name")
        print("2 - Change task status")
        print("3 - Display task")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == '1':
            set_task_name(task)
        elif choice == '2':
            change_task_status(task)
        elif choice == '3':
            display_task(task)
        elif choice == '0':
            break

    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()




            



