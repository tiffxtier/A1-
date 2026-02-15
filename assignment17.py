def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))


list1_input = input("Enter the first list of numbers separated by spaces: ")
list2_input = input("Enter the second list of numbers separated by spaces: ")

try:
    list1 = [int(x) for x in list1_input.split()]
    list2 = [int(x) for x in list2_input.split()]

    common = find_common_elements(list1, list2)
    print("Common elements:", common)

except ValueError:
    print("Input must contain only numbers.")
