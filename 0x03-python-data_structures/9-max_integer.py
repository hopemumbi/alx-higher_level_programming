#!/usr/bin/python3
def max_integer(my_list=[]):
    """ a function that finds the biggest integer of a list.

    Args:
        my_list: a list of integers

    Return:
        the biggest integer
    """
    # If the list is empty then
    if len(my_list) == 0:
        # return none
        return None
    else:
        # sort the list in ascending order
        my_list.sort()
        # the number at the last index
        return my_list[-1]
