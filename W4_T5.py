def multiply_digits(n):
    digits = [int(d) for d in str(n)]
    result = 1
    for d in digits:
        result *= d
    return result

print("Program starting.\n")

print("Check multiplicative persistence.")
n = int(input("Insert integer: "))
steps = 0

while n >= 10:
    print(" * ".join(str(d) for d in str(n)), end=' = ')
    n = multiply_digits(n)
    print(n)
    steps += 1

print(f"This program took {steps} step(s)\n")

print("Program ending.")
