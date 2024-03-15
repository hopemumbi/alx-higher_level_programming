#!/usr/bin/python3
def no_c(my_string):
    """function that removes all characters c and C from a string.

    Args:
        my_string: string to be edited

    Return:
        The string with all 'c' and 'C' characters removed.

    """
    # initialize an empty string
    new_string = ""
    # iterate through every character of the string
    for i in range(len(my_string)):
        # Check if the character at index i is 'c' or 'C'
        if my_string[i] != 'c' and my_string[i] != 'C':
            # If it is not, return a new string that excludes this character
            new_string += my_string[i]
    # return the original string
    return new_string
