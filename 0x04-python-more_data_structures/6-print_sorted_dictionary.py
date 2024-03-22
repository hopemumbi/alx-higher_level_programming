#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function that returns the number of keys in a dictionary.


    Args:
        a_dictionary: a dictionary
    """
    # sort by alphabetical order
    keys = sorted(a_dictionary)
    # iterate through the list of keys
    for i in keys:
        # print the key and its value
        print('{}: {}'.format(i, a_dictionary[i]))
