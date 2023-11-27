def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        number = float(line)
                        numbers.append(number)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("File not found.")
    return numbers

def calculate_statistics(numbers):
    total = round(sum(numbers), 2)
    count = len(numbers)
    average = round(total / count, 2) if count > 0 else 0.0
    return total, count, average

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    
    numbers = read_numbers_from_file(filename)
    
    if numbers:
        total, count, average = calculate_statistics(numbers)
        print("Results")
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
    else:
        print("No numbers found in the file.")
    
    print("Program ending.")
    return None


main()
