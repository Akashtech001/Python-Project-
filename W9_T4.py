from datetime import datetime

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def readTimestamps(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return [datetime.strptime(line.strip(), "%Y-%m-%dT%H:%M") for line in lines]

def calculateYears(year, timestamps):
    return sum(1 for timestamp in timestamps if timestamp.year == year)

def calculateMonths(month, timestamps):
    return sum(1 for timestamp in timestamps if MONTHS[timestamp.month - 1] == month)

def calculateWeekdays(weekday, timestamps):
    return sum(1 for timestamp in timestamps if WEEKDAYS[timestamp.weekday()] == weekday)

def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps = readTimestamps(filename)

    while True:
        print("Options:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            year = int(input("Insert year: "))
            count = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}': {count}\n")
        elif choice == "2":
            month = input("Insert month: ")
            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}': {count}\n")
        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}': {count}\n")
        elif choice == "0":
            print("\nProgram ending.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

