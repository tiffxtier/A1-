age_input = input("Enter your age: ")

if not age_input.isdigit():
    print("Age must be a positive integer.")
else:
    age = int(age_input)

    if age <= 0:
        print("Age must be a positive integer.")
    elif age < 18:
        print("Category: Minor")
    elif age <= 65:
        print("Category: Adult")
    else:
        print("Category: Senior citizen")
