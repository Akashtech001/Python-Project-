print("Program starting.\n")

word = input("Give a compound word: ")

length = len(word)
first_char = word[0]
reversed_word = word[::-1]

print(f"The word you gave is '{word}' and in reverse it is '{reversed_word}'.")
print(f"The given word length is: {length}")
print(f"Last character is: {word[-1]}\n")

start = int(input("Take substring from the inserted word by inserting...\n1) starting point: "))
end = int(input("2) ending point: "))
step = int(input("3) step size: "))

substring = word[start:end:step]

print(f"The word '{word}' sliced to the defined substring is '{substring}'")
print("Program ending.")
