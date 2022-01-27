def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    input_string = input_string.lower()
    # Traverse through each letter of the input string
    for i in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if i != " ":
            new_string = new_string + i
            reverse_string = i + reverse_string  # if you think both operations are same, then see magic by writing on paper.
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
