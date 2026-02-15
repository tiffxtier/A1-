def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:
        result = 1
        for _ in range(-exponent):
            result *= base
        return 1 / result


base_input = input("Enter the base (integer): ")
exp_input = input("Enter the exponent (integer): ")

if not base_input.lstrip("-").isdigit() or not exp_input.lstrip("-").isdigit():
    print("Both base and exponent must be integers.")
else:
    base = int(base_input)
    exponent = int(exp_input)
    print("Result:", power(base, exponent))
