print("Program starting.")
# Initialize variables to count words and characters
word_count = 0
char_count = 0
print()
while True:
    word = input("Insert word (empty stops): ")
    
    # Check if the input word is empty (blank)
    if not word:
        break
    
    # Update counts
    word_count += 1
    char_count += len(word)
print()
print(f"You inserted:")
print(f"- total words:  {word_count}")
print(f"- total characters:  {char_count}")
print()
print("Program ending.")
