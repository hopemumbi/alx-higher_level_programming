#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2


        Args:
            a_dictionary: dictionary to analyze

        Return:
            a_dictionary times two
    """
    # list the keys
    keys = list(a_dictionary)
    # iterate through the list of keys
    for i in keys:
        a_dictionary[i] = (a_dictionary[i])*2
    return a_dictionary
