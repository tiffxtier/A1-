rows_input = input("Enter the number of rows: ")
char = input("Enter the character to use for the pattern: ")

if not rows_input.isdigit():
    print("Number of rows must be a positive integer.")
elif len(char) != 1:
    print("Please enter exactly one character.")
else:
    rows = int(rows_input)

    if rows <= 0:
        print("Number of rows must be a positive integer.")
    else:
        for i in range(1, rows + 1):
            for j in range(i):
                print(char, end="")
            print()
