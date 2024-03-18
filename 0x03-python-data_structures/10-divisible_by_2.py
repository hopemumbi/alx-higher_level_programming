#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list.

    Args:
        my_list: list to be analyzed

    Return:
        a new list with True or False, depending on if a multiple is found
    """
    # initialize a new_list which is empty
    new_list = []
    # iterate through the original list
    for i in my_list:
        # if a multipe of 2 is found then
        if i % 2 == 0:
            # set it to true
            # append true to the new list
            new_list.append(True)
        # else set it to false
        else:
            # append false to the new list
            new_list.append(False)

    # return the new list
    return new_list
