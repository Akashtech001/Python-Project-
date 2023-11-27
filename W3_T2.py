print("Program starting.")
print("String comparisons")
word1 = input("Insert word: ")
char = input("Insert character: ")


if char in word1:
    print(f'Word "{word1}" contains character "{char}"')
else:
    print(f'Word "{word1}" doesn\'t contain character "{char}"')

print("")
    
print("Insert one more word")
word2=input("Insert word: ")

if word1 < word2:
    print(f'"{word1}" word is before the "{word2}" word in alphabetic order.')
elif word1 > word2:
    print(f'"{word2}" word is before the "{word1}" word in alphabetic order.')
else:
    print(f'Both words are the same, "{word1}"')
print("Program ending.")
