#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary.


    Args:
        a_dictionary: dictonary to be analyzed
        key: argument will be always a string
        value:  argument will be any type
    """
    a_dictionary[key] = value
    return a_dictionary
