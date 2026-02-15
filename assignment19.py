def sort_list(numbers):
    sorted_numbers = numbers[:]  # make a copy so original list is unchanged

    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # swap
                temp = sorted_numbers[j]
                sorted_numbers[j] = sorted_numbers[j + 1]
                sorted_numbers[j + 1] = temp

    return sorted_numbers


try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]

    result = sort_list(numbers)
    print("Sorted list:", result)

except ValueError:
    print("Please enter valid numbers only.")
