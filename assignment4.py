import math

x1_input = input("Enter x1: ")
y1_input = input("Enter y1: ")
x2_input = input("Enter x2: ")
y2_input = input("Enter y2: ")

if not x1_input.replace('.', '', 1).isdigit():
    print("Invalid input for x1.")
elif not y1_input.replace('.', '', 1).isdigit():
    print("Invalid input for y1.")
elif not x2_input.replace('.', '', 1).isdigit():
    print("Invalid input for x2.")
elif not y2_input.replace('.', '', 1).isdigit():
    print("Invalid input for y2.")
else:
    x1 = float(x1_input)
    y1 = float(y1_input)
    x2 = float(x2_input)
    y2 = float(y2_input)

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Distance between the two points:", distance)
