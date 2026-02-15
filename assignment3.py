weight_input = input("Enter your weight in kilograms: ")
height_input = input("Enter your height in meters: ")

if not weight_input.replace('.', '', 1).isdigit():
    print("Invalid input for weight.")
elif not height_input.replace('.', '', 1).isdigit():
    print("Invalid input for height.")
else:
    weight = float(weight_input)
    height = float(height_input)

    if weight <= 0:
        print("Weight must be a positive number.")
    elif height <= 0:
        print("Height must be a positive number.")
    else:
        bmi = weight / (height ** 2)
        print("Your BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
