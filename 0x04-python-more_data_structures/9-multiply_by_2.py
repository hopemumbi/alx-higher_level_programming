#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2


        Args:
            a_dictionary: dictionary to analyze

        Return:
            a_dictionary times two
    """
    # copy to a new dictionary
    new_dictionary = a_dictionary.copy()
    # list the keys
    keys = list(new_dictionary)
    # iterate through the list of keys
    for i in keys:
        new_dictionary[i] = (new_dictionary[i])*2
    # return the new dictionary
    return new_dictionary
