text = input("Enter a string: ")

if len(text) == 0:
    print("Input cannot be empty.")
else:
    left = 0
    right = len(text) - 1
    is_palindrome = True

    while left < right:
        if text[left] != text[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    if is_palindrome:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
