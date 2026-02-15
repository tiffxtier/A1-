mark1_input = input("Enter mark for subject 1: ")
mark2_input = input("Enter mark for subject 2: ")
mark3_input = input("Enter mark for subject 3: ")

if not mark1_input.replace('.', '', 1).isdigit():
    print("Invalid input for subject 1.")
elif not mark2_input.replace('.', '', 1).isdigit():
    print("Invalid input for subject 2.")
elif not mark3_input.replace('.', '', 1).isdigit():
    print("Invalid input for subject 3.")
else:
    mark1 = float(mark1_input)
    mark2 = float(mark2_input)
    mark3 = float(mark3_input)

    if mark1 < 0 or mark1 > 100:
        print("Subject 1 mark must be between 0 and 100.")
    elif mark2 < 0 or mark2 > 100:
        print("Subject 2 mark must be between 0 and 100.")
    elif mark3 < 0 or mark3 > 100:
        print("Subject 3 mark must be between 0 and 100.")
    else:
        average = (mark1 + mark2 + mark3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        print("Average:", average)
        print("Grade:", grade)
