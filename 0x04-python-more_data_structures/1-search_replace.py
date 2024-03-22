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
    # create an empty list new_list
    new_list = []
    # for element in my_list
    for i in my_list:
        # if element is equal to search
        if i == search:
            # add replace to new_list
            new_list.append(replace)
        # if not add the original element to new_list
        else:
            new_list.append(i)
    # return the new_list
    return new_list
