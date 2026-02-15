time_input = input("Enter time duration in hours: ")

if not time_input.replace('.', '', 1).isdigit():
    print("Invalid input for time duration.")
else:
    hours = float(time_input)

    if hours < 0:
        print("Time duration must be a non-negative number.")
    else:
        minutes = hours * 60
        seconds = hours * 3600

        print("Time in minutes:", minutes)
        print("Time in seconds:", seconds)
