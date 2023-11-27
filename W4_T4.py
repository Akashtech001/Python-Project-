print("Program starting.")
start = int(input("\nInsert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

if start >= stop:
    print("\nStarting point value must be less than the stopping point value.")
if not start <= inspect <= stop:
    print("Inspection value must be within the range of start and stop.")
elif start < stop and start <= inspect <= stop:
    print("\nFirst loop - inspection with break:")
    output = []
    for i in range(start, stop+1):
        output.append(str(i))
        if i == inspect:
            break
    print(' '.join(output))
    
    print("\nSecond loop - inspection with continue:")
    output = []
    for i in range(start, stop+1):
        if i == inspect:
            continue
        output.append(str(i))
    if output:
        print(' '.join(output))

if start < stop and start <= inspect <= stop or start >= stop or not start <= inspect <= stop:
    print("\nProgram ending.")
else:
    print("Program ending.")

