# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Taking input from the user
char = input("Enter a character: ")

# Checking if the character is a vowel using a for loop
is_vowel = False
for vowel in vowels:
    if char == vowel:
        is_vowel = True
        break  # No need to check further once a match is found

# Displaying the result
if is_vowel:
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is not a vowel.")

