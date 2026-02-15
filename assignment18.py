def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2


try:
    tuple1_input = input("Enter the first tuple elements separated by spaces: ")
    tuple2_input = input("Enter the second tuple elements separated by spaces: ")

    tuple1 = tuple(int(x) for x in tuple1_input.split())
    tuple2 = tuple(int(x) for x in tuple2_input.split())

    result = concat_tuples(tuple1, tuple2)
    print("Concatenated tuple:", result)

except ValueError:
    print("Input must contain only numbers.")
