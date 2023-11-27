class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

def display_todos(todos):
    print("TODOs:")
    for task in todos:
        status = "[x]" if task.done else "[.]\n"
        print(f" - {status} {task.name}")

def insert_task(todos, task_name):
    todos.append(Task(task_name))

def mark_done(todos, task_number):
    if 1 <= task_number <= len(todos):
        todos[task_number - 1].done = True
        print(f"Task '{todos[task_number - 1].name}' marked as done.")
    else:
        print("Invalid task number.")

def main():
    print("Program starting.")
    print("Welcome to the TODO app!")

    todos = []

    while True:
        print("Options:")
        print("1 - Insert task")
        print("2 - Mark done")
        print("3 - Display todos")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            task_name = input("Insert task name: \n")
            insert_task(todos, task_name)
        elif choice == "2":
            print("Currently incomplete TODOs:")
            task_number = int(input("Insert task number to mark it done: "))
            mark_done(todos, task_number)
        elif choice == "3":
            display_todos(todos)
        elif choice == "0":
            print("Program ending.")
            return None
        else:
            print("Invalid choice. Please try again.")

    # Operate
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()
