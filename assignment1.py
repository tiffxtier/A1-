principal_input = input("Enter the principal amount: ")
rate_input = input("Enter the interest rate (in percentage): ")
time_input = input("Enter the time period (in years): ")

if not principal_input.replace('.', '', 1).isdigit():
    print("Invalid input for principal amount.")
elif not rate_input.replace('.', '', 1).isdigit():
    print("Invalid input for interest rate.")
elif not time_input.replace('.', '', 1).isdigit():
    print("Invalid input for time period.")
else:
    principal = float(principal_input)
    rate = float(rate_input)
    time = float(time_input)

    simple_interest = (principal * rate * time) / 100
    print("Simple Interest:", simple_interest)
