#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """function that deletes a key in a dictionary.


    Args:
        a_dictionary: dictionary to be analyzed

    Return:
        a_dictionary after deletion
    """
    # check if key is in dictionary then
    if key in a_dictionary:
        # delete the key
        del a_dictionary[key]
    # return the dictionary after deletion
    return a_dictionary
