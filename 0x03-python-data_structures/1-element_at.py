#!/usr/bin/python3
def element_at(my_list, idx):
    """function that retrieves an element from a list like in C.
    Args:
        my_list: The list
        idx: index of the element to be retrived
    """
    # If idx is negative, the function should return None
    # else If idx is out of range > the function should return None
    if idx < 0 or idx >= len(my_list):
        return None
    # else return the item at the index
    else:
        return my_list[idx]
