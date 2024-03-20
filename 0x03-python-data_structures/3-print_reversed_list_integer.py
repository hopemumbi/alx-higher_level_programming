#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.

    Args:
        my_list: List to be reversed
    """
    if my_list is None:
        return my_list
    # Create a copy of the list
    new_list = my_list.copy()
    # reverse the copied list
    new_list.reverse()
    # iterate through the reversed list
    for i in range(len(new_list)):
        # print one integer per line
        print("{:d}".format(new_list[i]))
