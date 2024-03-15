#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element without modifying the original list

    Args:
        my_list: The original list
        idx: index to be modified
        element: the element that acts as a replacement

    Return:
        a copy of the original list is idx < 0 or out of range
        otherwise the new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
