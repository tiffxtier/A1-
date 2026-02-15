def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


user_input = input("Enter a string: ")

if len(user_input) == 0:
    print("Input cannot be empty.")
else:
    if is_palindrome(user_input):
        print("True")
    else:
        print("False")
