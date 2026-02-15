number_input = input("Enter a positive integer: ")

if not number_input.isdigit():
    print("Input must be a positive integer.")
else:
    number = int(number_input)

    if number <= 0:
        print("Input must be a positive integer.")
    else:
        print("Collatz sequence:")

        while number != 1:
            print(number, end=" ")

            if number % 2 == 0:
                number = number // 2
            else:
                number = number * 3 + 1

        print(1)
