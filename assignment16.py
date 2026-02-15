def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number_input = input("Enter a positive integer: ")

if not number_input.isdigit():
    print("Input must be a positive integer.")
else:
    number = int(number_input)

    if is_prime(number):
        print("True")
    else:
        print("False")
