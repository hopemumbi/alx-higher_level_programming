#!/usr/bin/bash


def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position

    Args:
        my_list: The list of integers.
        idx: index to replace
        element: new element to replace at index idx.

    Return:
        Original list (idx < 0 or out of range), otherwise  the editited list
    """
    # If idx is negative or If idx is out of range then
    if idx < 0 or idx >= len(my_list):
        # returns the original list
        return my_list
    # Replace the element at index idx with the new element
    my_list[idx] = element
    return my_list
