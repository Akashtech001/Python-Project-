print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

W1_T1 = int(input("W1_T1: "))
W1_T2 = int(input("W1_T2: "))
W1_T3 = int(input("W1_T3: "))
W1_T4 = int(input("W1_T4: "))
W1_T5 = int(input("W1_T5: "))

total_time = W1_T1 + W1_T2 + W1_T3 + W1_T4 + W1_T5
average_time = total_time / 5

print(f"\nIn total you spent {total_time} minutes on programming.")
print(f"Average per task was {average_time:.1f} min and same rounded to the nearest integer {round(average_time)} min.\n")
print("Program ending.")
