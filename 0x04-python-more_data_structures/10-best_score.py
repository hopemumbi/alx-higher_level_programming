#!/usr/bin/python3
def best_score(a_dictionary):
    """function that returns a key with the biggest integer value.


    Args:
        a_dictionary: dictionary to analyze
    Return:
        the key with the highest value
    """
    # check if dictionary is empty
    if a_dictionary is None:
        return None
    else:
        # list the keys in the dictionary then
        # iterate through the list and return their values
        a = [a_dictionary[i] for i in list(a_dictionary)]
        # sort the values in ascending order
        a.sort()
        # iterate through the dictionary
        # use item() to access both the key and value
        # if the key value is highest
        for key, value in a_dictionary.items():
            if value == a[-1]:
                # return the key
                return key
