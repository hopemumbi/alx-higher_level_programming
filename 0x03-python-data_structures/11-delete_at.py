#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """function that deletes the item at a specific position in a list.

    Args:
        my_list: list to be analyzed
        idx: index to perform deletion

    Return:
        return a new list after deletion
    """
    # check if idx is < 0 or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # delete at index idx
        del my_list[idx]
        # return the new list
        return my_list
