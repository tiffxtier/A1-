char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
elif not char.isalpha():
    print("Input must be a letter.")
else:
    char = char.lower()

    if char in ['a', 'e', 'i', 'o', 'u']:
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
