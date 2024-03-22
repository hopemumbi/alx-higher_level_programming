#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element
        by another in a new list.


    Args:
        my_list: the initial list
        search: the element to replace in the lis
        replace: the new element

    Return:

    """
    # create a copy of the original list
    new_list = my_list.copy()
    # find the index of search and assign that position replace
    new_list[new_list.index(search)] = replace
    # return the new list
    return(new_list)
